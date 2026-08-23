#!/usr/bin/env python3
"""
AI-Driven API Test Generator
Student: Le Tuan Lok (23127404)
Course: Software Testing (CS300) — FIT HCMUS
Module: Agent Skill (Bloom-AI Level G9.5 Create)
"""
import os, sys
# Relay to parent generator.py
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from generator import main

if __name__ == "__main__":
    main()
