import openai

openai.api_key = "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"

def suggest_specialists(project_description):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="In your project, based on the description '" + customer_description + "', what specialist roles should you have?",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response["choices"][0]["text"].strip()
    return message

customer_description = input("Please enter a description of your project: ")
specialist_advice = suggest_specialists(customer_description)
print("Advice:", specialist_advice)