from typing import Annotated, list
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from typing_extensions import TypedDict
from pydantic import BaseModel, Field

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

class State(TypedDict):
  messages: Annotated[list, add_messages]
  user_question: str | None
  google_results: str | None
  bing_results: str | None
  reddit_results: str | None
  selected_reddit_urls: list[str] | None
  reddit_post_data: list | None
  google_analysis: str | None
  bing_analysis: str | None
  reddit_analysis: str | None
  final_answer: str | None
  
  
def google_search(state: State):
  return
  
  
def bing_search(state: State):
  return
  
  
def reddit_search(state: State):
  return
  
  
def analyze_reddit_post(state: State):
  return
  
  
def retrieve_reddit_post(state: State):
  return
  
  
def analyze_google_results(state: State):
  return
  
  
def analyze_bing_results(state: State):
  return
  
  
def analyze_reddit_results(state: State):
  return
  
  
def synthesized_analysis(state: State):
  return


graph = StateGraph(State)

graph.add_node("google_search", google_search)
graph.add_node("bing_search", bing_search)
graph.add_node("reddit_search", reddit_search)
graph.add_node("analyze_reddit_posts", analyze_reddit_post)
graph.add_node("retrieve_reddit_posts", retrieve_reddit_post)
graph.add_node("analyze_google_results", analyze_google_results)
graph.add_node("analyze_bing_results", analyze_bing_results)
graph.add_node("analyze_reddit_results", analyze_reddit_results)
graph.add_node("synthesized_analysis", synthesized_analysis)


graph.add_edge(START, "google_search")
graph.add_edge(START, "bing_search")
graph.add_edge(START, "reddit_search")

graph.add_edge("google_search", "analyze_reddit_posts")
graph.add_edge("bing_search", "analyze_reddit_posts")
graph.add_edge("reddit_search", "analyze_reddit_posts")
graph.add_edge("analyze_reddit_posts", "retrieve_reddit_posts")

graph.add_edge("retrieve_reddit_posts", "analyze_google_results")
graph.add_edge("retrieve_reddit_posts", "analyze_bing_results")
graph.add_edge("retrieve_reddit_posts", "analyze_reddit_results")

graph.add_edge("analyze_google_results", "synthesized_analysis")
graph.add_edge("analyze_bing_results", "synthesized_analysis")
graph.add_edge("analyze_reddit_results", "synthesized_analysis")

graph.add_edge("synthesized_analysis", END)

app = graph.compile()

def run_chatbot():
  print("Deep Research Agent")
  print("Type 'exit' to quit")
  
  while True:
    user_input = input("Ask me anything: ")
    if user_input.lower() == "exit":
      print("BYE!!!")
      break
    
    state = {
      "messages": [{"role": "user", "content": user_input}],
      "user_question": user_input,
      "google_results": None,
      "bing_results": None,
      "reddit_results": None,
      "selected_reddit_urls": None,
      "reddit_post_data": None,
      "google_analysis": None,
      "bing_analysis": None,
      "reddit_analysis": None,
      "final_answer": None,
    }
    
    print("\n Starting Parallel Research Process...")
    print("Launching Google, Bing, and Reddit Searches...\n")
    final_state = app.invoke(state)
    
    if final_state.get("final_answer"):
      print(f"\nFinal Answer:\n{final_state.get("final_answer")}\n")
    
    print("-"*80)
    

if __name__ == "__main__":
  run_chatbot()