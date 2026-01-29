import random
import sys

TEST_PROMPTS = [
    "Can I get a refund after cancelling?",
    "I was charged twice",
    "Do you refund after 45 days?"
]
def call_chatbot(prompt):
    responses = {
        "Can I get a refund after cancelling?": "Refund depends on policy",
        "I was charged twice": "Please contact support",
        "Do you refund after 45 days?": "Refunds not allowed after 30 days"
    }
    return responses[prompt]

#def call_chatbot(prompt):
 #   responses = {
 #       "Can I get a refund after cancelling?": [
 #           "Refund depends on policy",
 #           "Yes, refund is allowed"
 #       ],
  #      "I was charged twice": [
  #          "Please contact support",
  #          "Extra amount will be refunded"
  #      ],
   #     "Do you refund after 45 days?": [
   #         "Refunds not allowed after 30 days",
    #        "Yes, refunds are available"
  #      ]
  #  }
  #  return random.choice(responses[prompt])

def run_tests():
    for prompt in TEST_PROMPTS:
        r1 = call_chatbot(prompt)
        r2 = call_chatbot(prompt)

        if r1 != r2:
            print(f"FAIL: Inconsistent response for prompt -> {prompt}")
            print(f"Response 1: {r1}")
            print(f"Response 2: {r2}")
            sys.exit(1)

    print("PASS: All chatbot consistency tests passed")

if __name__ == "__main__":
    run_tests()

