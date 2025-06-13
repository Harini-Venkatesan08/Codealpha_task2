import tkinter as tk

# Flipkart FAQ database
faq_data = {
    "How do I track my Flipkart order?":
        "Go to 'My Orders' > Select the order > Tap 'Track' to view real-time updates.",
    "How do I cancel an order?":
        "Visit 'My Orders' > Choose the order > Click 'Cancel' and select a reason.",
    "What is Flipkart’s return policy?":
        "Most items can be returned within 7–10 days. Check the item's return policy for details.",
    "How can I contact Flipkart customer support?":
        "Go to Help Center on the Flipkart app or website and select your issue.",
    "How do I apply a coupon or discount code?":
        "During checkout, tap 'Apply Coupon' and enter your promo code.",
    "How do I change my delivery address?":
        "Before placing an order, you can change or add a new address in your profile.",
    "Why was my order delayed?":
        "Delivery delays may happen due to high demand, weather, or logistical issues.",
    "What payment methods does Flipkart accept?":
        "Flipkart accepts UPI, debit/credit cards, net banking, and Cash on Delivery (COD).",
    "How do I return a defective product?":
        "Go to 'My Orders' > Select the product > Click 'Return' and choose the reason.",
    "How do I know if a seller is trustworthy?":
        "Check ratings, reviews, and 'Flipkart Assured' tag for verified sellers."
}

# GUI setup
root = tk.Tk()
root.title("FAQ Chatbot - Flipkart")
root.geometry("600x450")

# Title label
title_label = tk.Label(root, text="🛒 Flipkart FAQ Chatbot", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Dropdown menu
question_var = tk.StringVar(root)
question_var.set("Select a question")

def show_dropdown_answer(*args):
    selected = question_var.get()
    if selected in faq_data:
        response_label.config(text="Bot: " + faq_data[selected])
    else:
        response_label.config(text="")

dropdown = tk.OptionMenu(root, question_var, *faq_data.keys())
dropdown.config(width=60, font=("Arial", 11))
dropdown.pack(pady=10)

question_var.trace("w", show_dropdown_answer)

# Response display label
response_label = tk.Label(root, text="", wraplength=550, font=("Arial", 12), fg="blue", justify="left")
response_label.pack(pady=10)

# Manual input
entry_label = tk.Label(root, text="Or ask your own question below:", font=("Arial", 12))
entry_label.pack(pady=5)

manual_entry = tk.Entry(root, font=("Arial", 12), width=60)
manual_entry.pack(pady=5)

# Ask button
def answer_manual_question():
    user_question = manual_entry.get().strip().lower()
    found = False
    for q, a in faq_data.items():
        if user_question in q.lower():
            response_label.config(text="Bot: " + a)
            found = True
            break
    if not found:
        response_label.config(text="Bot: Sorry, I don't have an answer for that.")

ask_btn = tk.Button(root, text="Ask", command=answer_manual_question, font=("Arial", 12))
ask_btn.pack(pady=10)

root.mainloop()
