import { expect, type APIRequestContext, type APIResponse } from "@playwright/test";
import type { OrderStatus } from "./types.js";

const API_URL = process.env.API_URL ?? "http://localhost:3000/api";

export class ApiDriver {
  constructor(private readonly request: APIRequestContext) {}

  async login(email: string, password: string): Promise<string> {
    const response = await this.request.post(`${API_URL}/login`, {
      data: { email, password },
    });
    expect(response.ok(), `Login failed for ${email}: ${await response.text()}`).toBeTruthy();
    const body = (await response.json()) as { token: string };
    expect(body.token).toBeTruthy();
    return body.token;
  }

  headers(token?: string): Record<string, string> {
    return token ? { Authorization: `Bearer ${token}` } : {};
  }

  async createPendingOrder(userToken: string): Promise<number> {
    const response = await this.request.post(`${API_URL}/checkout`, {
      headers: this.headers(userToken),
      data: {
        total_amount: 30000000,
        shipping_address: `HW04 isolated order ${crypto.randomUUID()}`,
      },
    });
    expect(response.status()).toBe(200);
    const body = (await response.json()) as { orderId: number };
    return body.orderId;
  }

  async adminTransition(orderId: number, status: OrderStatus, adminToken: string): Promise<APIResponse> {
    return this.request.put(`${API_URL}/admin/orders/${orderId}/status`, {
      headers: this.headers(adminToken),
      data: { status },
    });
  }

  async userCancel(orderId: number, userToken: string): Promise<APIResponse> {
    return this.request.put(`${API_URL}/orders/${orderId}/cancel`, {
      headers: this.headers(userToken),
      data: {},
    });
  }

  async getOrder(orderId: number): Promise<{ status: OrderStatus }> {
    const response = await this.request.get(`${API_URL}/orders/${orderId}`);
    expect(response.status()).toBe(200);
    return (await response.json()) as { status: OrderStatus };
  }

  async arrangeOrder(
    setup: OrderStatus[],
    userToken: string,
    adminToken: string,
  ): Promise<number> {
    const orderId = await this.createPendingOrder(userToken);
    for (const state of setup) {
      const response = await this.adminTransition(orderId, state, adminToken);
      expect(
        response.status(),
        `Could not arrange order ${orderId} into ${state}: ${await response.text()}`,
      ).toBe(200);
    }
    return orderId;
  }
}
