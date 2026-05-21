class KnowledgeBase:
    def __init__(self):
        # Simulate a local knowledge base with predefined documents
        self.documents = [
            "ICECODE is a self-hosted AI agent platform designed for data privacy and operational control.",
            "It supports multi-agent swarms, allowing multiple AI agents to collaborate on complex tasks.",
            "Local RAG (Retrieval Augmented Generation) is a core feature, enabling agents to use company-specific, local data.",
            "ICECODE provides a comprehensive web interface for managing agents and workflows.",
            "Key benefits include enhanced data security, customization flexibility, and automation of business processes.",
            "Unlike cloud-based solutions, ICECODE keeps sensitive data within your own infrastructure."
        ]

    def retrieve(self, query: str) -> list[str]:
        """Simulates retrieving relevant documents based on keywords in the query."""
        relevant_chunks = []
        # Simple keyword matching for retrieval
        query_keywords = [word.lower() for word in query.split() if len(word) > 2]
        
        for doc in self.documents:
            if any(keyword in doc.lower() for keyword in query_keywords):
                relevant_chunks.append(doc)
        return list(set(relevant_chunks)) # Return unique chunks

class RetrievalAgent:
    def __init__(self, kb: KnowledgeBase):
        self.knowledge_base = kb

    def retrieve_information(self, query: str) -> str:
        """This agent retrieves information from the local knowledge base (simulating local RAG)."""
        print(f"Retrieval Agent: Searching for '{query}'...")
        chunks = self.knowledge_base.retrieve(query)
        if chunks:
            retrieved_text = "\n".join(chunks)
            print(f"Retrieval Agent: Found relevant information.")
            return retrieved_text
        else:
            print(f"Retrieval Agent: No specific information found.")
            return ""

class GenerationAgent:
    def __init__(self, model_name="MockLLM"):
        self.model_name = model_name

    def generate_response(self, query: str, context: str) -> str:
        """This agent simulates an LLM generating a response, using retrieved context if available."""
        print(f"Generation Agent: Generating response for '{query}' with context...")
        
        if context: # If context was retrieved by the RetrievalAgent
            # Simulate RAG: integrate context into the response
            if "what is icecode" in query.lower():
                return f"Based on the retrieved information: {context.split('.')[0]}. It also supports multi-agent swarms and local RAG for data privacy."
            elif "benefits" in query.lower():
                return f"From the context provided: {context.split('Key benefits include')[1].split('.')[0]}."
            elif "rag" in query.lower():
                return f"The context mentions: {context.split('Local RAG')[1].split('.')[0]}. This enables agents to use company-specific, local data."
            else:
                return f"I can answer your query '{query}' using the provided context: {context}"
        else:
            # Simulate a generic LLM response without specific context
            return f"I understand you asked about '{query}'. Without specific context, I can provide a general answer: AI agent platforms help automate tasks and manage complex workflows."

def main():
    print("--- Starting ICECODE-like Multi-Agent RAG Simulation ---")
    
    # Initialize the local knowledge base for RAG
    kb = KnowledgeBase()
    
    # Initialize our two distinct agents
    retrieval_agent = RetrievalAgent(kb)
    generation_agent = GenerationAgent()
    
    # --- Scenario 1: Query with relevant information in KB ---
    user_query_1 = "What is ICECODE and its main features?"
    print(f"\nUser: {user_query_1}")
    
    # Agent 1: Retrieve relevant information (simulating local RAG)
    retrieved_context_1 = retrieval_agent.retrieve_information(user_query_1)
    
    # Agent 2: Generate a response using the retrieved context
    final_response_1 = generation_agent.generate_response(user_query_1, retrieved_context_1)
    print(f"AI Assistant: {final_response_1}")

    # --- Scenario 2: Query about benefits ---
    user_query_2 = "What are the benefits of using ICECODE?"
    print(f"\nUser: {user_query_2}")
    
    retrieved_context_2 = retrieval_agent.retrieve_information(user_query_2)
    final_response_2 = generation_agent.generate_response(user_query_2, retrieved_context_2)
    print(f"AI Assistant: {final_response_2}")

    # --- Scenario 3: Query with less specific information in KB (or no direct match) ---
    user_query_3 = "Tell me about AI agent platforms in general."
    print(f"\nUser: {user_query_3}")
    
    retrieved_context_3 = retrieval_agent.retrieve_information(user_query_3)
    final_response_3 = generation_agent.generate_response(user_query_3, retrieved_context_3)
    print(f"AI Assistant: {final_response_3}")

    print("\n--- Simulation Finished ---")

if __name__ == "__main__":
    main()
