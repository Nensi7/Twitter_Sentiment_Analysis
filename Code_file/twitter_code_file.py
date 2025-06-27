# enhanced_tweet_gui.py
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

# --- Load dataset ---
df = pd.read_csv("D:/sample_1000_tweets_sentiment.csv", parse_dates=["date"])
# Ensure your CSV has columns: date, text, sentiment

# --- Colors by sentiment ---
COLORS = {
    "positive": "green",
    "neutral": "gray",
    "negative": "red"
}

# --- Main window setup ---
root = tk.Tk()
root.title("Tweet Sentiment Explorer")
root.geometry("800x550")
root.resizable(False, False)

# --- Top frame: Date input ---
frm_input = ttk.Frame(root, padding=10)
frm_input.pack(fill="x")
ttk.Label(frm_input, text="Enter date (YYYY-MM-DD):").pack(side="left")
date_var = tk.StringVar()
ttk.Entry(frm_input, width=15, textvariable=date_var).pack(side="left", padx=5)
ttk.Button(frm_input, text="Load Tweets", command=lambda: on_load()).pack(side="left", padx=5)

# --- Center frame: Listbox + Tweet view ---
frm_center = ttk.Frame(root)
frm_center.pack(fill="both", expand=True, padx=10, pady=5)

listbox = tk.Listbox(frm_center, width=45, height=20)
scroll_list = ttk.Scrollbar(frm_center, orient="vertical", command=listbox.yview)
listbox.configure(yscrollcommand=scroll_list.set)
listbox.grid(row=0, column=0, sticky="ns")
scroll_list.grid(row=0, column=1, sticky="ns")

txt_frame = ttk.LabelFrame(frm_center, text="Selected Tweet", padding=5)
txt_frame.grid(row=0, column=2, sticky="nsew", padx=10)
frm_center.columnconfigure(2, weight=1)

tweet_text = tk.Text(txt_frame, wrap="word", width=60, height=12, state="disabled")
tweet_text.pack(fill="both", expand=True)

# --- Sentiment label at bottom ---
sent_label = ttk.Label(root, text="Sentiment: ", font=("Arial", 14))
sent_label.pack(pady=10)

# --- Event handlers ---

def on_load():
    listbox.delete(0, tk.END)
    tweet_text.config(state="normal")
    tweet_text.delete(1.0, tk.END)
    tweet_text.config(state="disabled")
    sent_label.config(text="Sentiment: ", foreground="black")

    date_str = date_var.get().strip()
    try:
        sel_date = pd.to_datetime(date_str).date()
    except Exception:
        return messagebox.showerror("Invalid Date", "Please enter in YYYY-MM-DD format.")

    subset = df[df["date"].dt.date == sel_date]
    if subset.empty:
        return messagebox.showinfo("No Data", f"No tweets found on {sel_date}")
    for _, row in subset.iterrows():
        listbox.insert(tk.END, row["text"][:60] + "…")
    sent_label.config(text=f"{len(subset)} tweets on {sel_date}. Select one below.", foreground="black")

def on_select(event):
    idxs = listbox.curselection()
    if not idxs:
        return
    idx = idxs[0]
    short_text = listbox.get(idx)[:-1]
    row = df[df["text"].str.startswith(short_text)].iloc[0]

    tweet_text.config(state="normal")
    tweet_text.delete(1.0, tk.END)
    tweet_text.insert(tk.END, row["text"])
    tweet_text.config(state="disabled")

    sentiment = row["sentiment"]
    color = COLORS.get(sentiment, "black")
    sent_label.config(text=f"Sentiment: {sentiment.capitalize()}", foreground=color)

listbox.bind("<<ListboxSelect>>", on_select)

root.mainloop()
