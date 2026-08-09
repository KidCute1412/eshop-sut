export type Priority = "high" | "medium" | "low";

export interface TraceableCase {
  id: string;
  title: string;
  priority: Priority;
  partition: string[];
  boundary?: string[];
}

export type ProductAssertion =
  | "full-content"
  | "single-heading"
  | "image"
  | "price"
  | "description"
  | "category"
  | "quantity-type"
  | "quantity-min"
  | "quantity-default"
  | "add-feedback-first-click"
  | "add-feedback-valid-quantity"
  | "reject-zero"
  | "reject-negative"
  | "reject-fraction"
  | "not-found";

export interface ProductDetailCase extends TraceableCase {
  productId: number;
  assertion: ProductAssertion;
  quantity?: string;
  expected?: {
    name?: string;
    price?: string;
    description?: string;
    category?: string;
  };
}

export type OrderStatus =
  | "pending"
  | "confirmed"
  | "shipping"
  | "delivered"
  | "canceled";

export interface OrderTransitionCase extends TraceableCase {
  actor: "admin" | "user";
  setup: OrderStatus[];
  from: OrderStatus;
  to: OrderStatus;
  expectedStatus: number;
  expectedFinalState: OrderStatus;
}

export type AuthMode = "none" | "malformed" | "user" | "admin";
export type CleanupKind = "product" | "category" | "coupon";

export interface AccessControlCase extends TraceableCase {
  method: "GET" | "POST" | "PUT" | "DELETE";
  path: string;
  auth: AuthMode;
  expectedStatus: number;
  body?: Record<string, unknown>;
  cleanup?: CleanupKind;
}
