from google import genai
import sys

client = genai.Client(api_key="<API KEY HERE>")

prompt = " ".join(sys.argv[1:]) + " no explanation, just the code"


def prompt_function(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt,
    )
    return response.text

responses = prompt_function(prompt)
# Split the response into lines and remove the first and last lines
list_responses= responses.split("\n")
del list_responses[0]
del list_responses[-1]
del list_responses[-1]

#Writes in a file
file = open("test1.py", "w")
#merging the list into a single string after seperating overhead
file.write("\n".join(list_responses))
file.close()