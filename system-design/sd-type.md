# System Categories

## 1. Content Delivery & Social Systems
- Focus: Feed generation, content ranking, and user interaction
- Examples:
    - Design X (timeline service)
    - Instagram / TikTok (photo/video sharing, stories)
    - Reddit or Hacker News (voting and ranking)
    - YouTube (video streaming and recommendation)
- Concepts Tested:
    - Caching
    - CDN
    - Fan-out
    - Timelines
    - Ranking algorithms
    - Denormalized data stores

## 2. Messaging & Real-Time Systems
- Focus: High throughput, low latency, real-time communication
- Examples:
    - WhatsApp / Messenger (chat system)
    - Slack / Discord (group messaging)
    - Notification Service (push and in-app notifications)
    - Real-time collaboration tools (e.g., Google Docs)
- Concepts Tested:
    - WebSockets
    - Message queues (Kafka)
    - Real-time event handling
    - Pub/Sub
    - Consistency models

## 3. Storage & Data-Heavy Systems
- Focus: Large-scale storage, retrieval, and indexing
- Examples:
    - Dropbox / Google Drive (file storage)
    - YouTube (video storage)
    - URL Shortener
    - Pastebin
- Concepts Tested:
    - Distributed file systems
    - Metadata management
    - Partitioning
    - Replication
    - Consistency

## 4. Search, Recommendation & Analytical Systems
- Focus: Query optimization and data pipeline design
- Examples:
    - Google Search
    - Netflix Recommendation System
    - Trending Topics Engine
    - Analytics Systems (e.g., Google Analytics)
- Concepts Tested:
    - Indexing
    - Inverted index
    - Ranking algorithms
    - Personalization
    - Data aggregation
    - Batch + stream processing

## 5. E-commerce, Booking & Transaction Systems
- Focus: Data integrity, inventory management, and concurrency
- Examples:
    - Amazon / eBay (e-commerce)
    - Uber / Lyft (ride-sharing)
    - Ticket Booking System (seat reservation)
    - Payment Service (Stripe, PayPal)
- Concepts Tested:
    - ACID vs eventual consistency
    - Transactions
    - Distributed locks
    - Queue-based processing
    - Idempotency

## 6. Infrastructure / Platform Systems
- Focus: Scalability, service orchestration, and reliability
- Examples:
    - Load Balancer
    - Rate Limiter
    - API Gateway
    - Distributed Cache (e.g., Redis)
    - Monitoring System
- Concepts Tested:
    - Reverse proxying
    - Service discovery
    - Fault tolerance
    - Distributed coordination

## 7. Event-Driven & Stream Processing Systems
- Focus: Real-time data pipelines
- Examples:
    - Kafka / Event Streaming Platforms
    - Metrics Collection System
    - ClickStream Processor
- Concepts Tested:
    - Message queues
    - Event sourcing
    - Stream vs Batch processing
    - Exactly-once semantics

## 8. Machine Learning / AI Serving Systems
- Focus: Model serving and feature management
- Examples:
    - ML Model Serving Platform
    - Feature Store
    - Recommendation API
- Concepts Tested:
    - Model versioning
    - Online/offline inference
    - Caching
    - A/B testing
    - Data drift handling