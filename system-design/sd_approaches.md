# Thought process for an SD-Interview 
Follow a structured top-down, iterative method combined with trade-off discussion
## Execution Steps
* Clarify Requirments
    * Functional requirments (WHAT a system should do)
    * Non-Functional requirements
        * Latency
        * Throughput
        * Availability
        * Consistency
* Define High Level Architecture
    * Identify the major component first
        * Client
        * API gateway/ Load Balancer
        * Core Services
        * Databse/ Cache / Queue system
    * Draw a high level blocking diagram
* Identify Data Flow
    * Map how data moves through the system
      * Highlight bottleneck and high-load points
* Deep Dive into key concepts
    * Service
    * Database
    * Queue/ Message system
    * Scalability strategies
* Discuss trade-offs
    * Explain the selection reason
        * Latency vs cost
        * Consistency vs availability
        * Complexity vs maintaibility
* Address Non Functionality Requirements
    * Think about
        * Scalability
        * Reliability /Fault tolerance
        * Monitoring / logging
        * Security and privacy
* Summarize / Iterate
    * Review your design
        * Recap components and flows
        * Revisit bottlenecks and trade-offs
        * Suggest possible improvements if time permits
## Key Points
* Structured top-down thinking
* Asking clarifying question upfront
* Clear diagram or sketeches
* Explicit trade-off decision
* Ability to iterate and refine the solution
* Considering non-function requirement

# Remember
[Clarify] → [High-Level] → [Data Flow] → [Deep Dive] → [Trade-Offs] → [Non-Functional] → [Summarize]


    