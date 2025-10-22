from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import GoogleGenerativeAI

from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')
os.environ['GOOGLE_API_KEY'] = google_api_key

# Initialize Gemini LLM
llm = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    # Prompt and chain for restaurant name
    prompt_template_name = PromptTemplate.from_template(
        "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this. Return only the restaurant name, nothing else."
    )
    name_chain = prompt_template_name | llm | StrOutputParser()

    # Prompt and chain for menu items, using the output of the first chain
    prompt_template_items = PromptTemplate.from_template(
        """Suggest some menu items for {restaurant_name}. Return it as a comma separated string only, no other text."""
    )
    food_items_chain = prompt_template_items | llm | StrOutputParser()

    # Combine the chains using RunnablePassthrough and RunnableParallel
    full_chain = (
        RunnablePassthrough.assign(restaurant_name=name_chain) |
        RunnableParallel(
            restaurant_name=lambda x: x['restaurant_name'].strip(),
            menu_items=food_items_chain
        )
    )

    response = full_chain.invoke({'cuisine': cuisine})
    
    # Format the response with proper introduction
    restaurant_name = response['restaurant_name']
    menu_items = response['menu_items'].strip()
    
    formatted_response = f"""🍽️ Here's a fancy name suggestion for your {cuisine} restaurant:

✨ **"{restaurant_name}"** ✨

📋 And here are some menu items for {restaurant_name}, as a comma-separated list:

{menu_items}"""
    
    return {
        'restaurant_name': restaurant_name,
        'menu_items': menu_items,
        'formatted_text': formatted_response
    }

if __name__ == "__main__":
    response = generate_restaurant_name_and_items("Italian")
    print(response['formatted_text'])
