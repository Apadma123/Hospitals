# 🏥 Healthcare Cost Navigator 

A minimal FastAPI-based web service that lets patients search hospitals by DRG code, ZIP code, and radius. It includes estimated prices, quality ratings, and a natural language AI assistant powered by OpenAI.

- 🔍 Search hospitals by MS-DRG code, ZIP, and radius
- 💰 View average charges & Medicare payments
- ⭐ See mock star ratings (1–10)
- 🤖 Ask natural language questions like:
  - “Who is cheapest for DRG 470 within 25 miles of 10001?”
  - “Which hospitals have the best ratings for heart surgery near 10032?”

---

## Tech Stack

- Python 3.11
- FastAPI
- Async SQLAlchemy
- PostgreSQL (via Docker)
- OpenAI GPT-4 (via API)
- Pandas, Geopy for ETL

---

## Quick Start

### 1. Clone and Set Up Environment

```bash
git clone https://github.com/your-username/healthcare-cost-navigator.git
cd healthcare-cost-navigator
cp .env.example .env
