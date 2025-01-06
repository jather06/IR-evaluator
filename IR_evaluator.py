from tkinter import *
from tkinter import messagebox   

       

list1 = [
    (1, "Top 10 Affordable Cities for Digital Nomads in 2025"),
    (1, "How to Manage Taxes as a Digital Nomad"),
    (0, "The Ultimate Guide to Backpacking Through Europe"),
    (1, "Best Co-Working Spaces in Bali"),
    (1, "Why Fast Internet Is Essential for Remote Work"),
    (0, "How to Start a Travel Vlog That Earns Money"),
    (1, "Challenges of Balancing Work and Travel as a Nomad"),
    (1, "Must-Have Gadgets for Digital Nomads"),
    (0, "Top Beach Destinations for Relaxation"),
    (1, "The Rise of Nomad Visas Worldwide")
]

list2 = [
    (1, "The Rise of Nomad Visas Worldwide"),
    (1, "Top 10 Affordable Cities for Digital Nomads in 2025"),
    (0, "How to Start a Travel Vlog That Earns Money"),
    (0, "Best Destinations for Digital Detox in 2025"),
    (1, "How to Manage Taxes as a Digital Nomad"),
    (1, "The Impact of Remote Work on Mental Health"),
    (1, "Challenges of Balancing Work and Travel as a Nomad"),
    (1, "Why Fast Internet Is Essential for Remote Work"),
    (1, "Best Co-Working Spaces in Bali"),
    (1, "How to Build a Passive Income While Traveling")
]

def calculate_metrics():
   relevant_docs = int(relevant_input.get())
   if relevant_docs <= 0:
       messagebox.showerror("Error", "Total relevant documents must be positive.")
       return
   
   def calculate_precision_recall(results, relevant_docs):
       hits = 0
       precision = []
       recall = []
       for i, (relevance, _) in enumerate(results):
           if relevance == 1:
                hits += 1
                precision.append(hits / (i + 1))
                recall.append(hits / relevant_docs)
       return precision, recall
   
    #aanroepen van de functie calculate_precision_recall voor beide lijsten.
   precision1, recall1 = calculate_precision_recall(list1, relevant_docs)   
   precision2, recall2 = calculate_precision_recall(list2, relevant_docs)
   
    #Formules voor het berekenen
   def f1(prec, rec):
        return (2 * prec * rec) / (prec + rec) if prec + rec > 0 else 0
   
   total_precision1 = sum(precision1) / len(precision1)
   total_recall1 = sum(recall1) / len(recall1)
   f1_measure1 = f1(total_precision1, total_recall1)
   avg_precision1 = sum(precision1) / len(precision1)
   precision_at_1_1 = precision1[0]
   
   total_precision2 = sum(precision2) / len(precision2)
   total_recall2 = sum(recall2) / len(recall2)
   f1_measure2 = f1(total_precision2, total_recall2)
   avg_precision2 = sum(precision2) / len(precision2)
   precision_at_1_2 = precision2[0]
   

    # Calculate overlap
   overlap = len(set([x[1] for x in list1]) & set([x[1] for x in list2]))


    # Display metrics
   metrics1_label.config(
        text=f"List 1 - Precision: {total_precision1:.2f}, Recall: {total_recall1:.2f}, F1: {f1_measure1:.2f}, "
             f"Precision@1: {precision_at_1_1:.2f}, Avg Precision: {avg_precision1:.2f}"
    )
   metrics2_label.config(
        text=f"List 2 - Precision: {total_precision2:.2f}, Recall: {total_recall2:.2f}, F1: {f1_measure2:.2f}, "
             f"Precision@1: {precision_at_1_2:.2f}, Avg Precision: {avg_precision2:.2f}"
    )
   overlap_label.config(text=f"Result Overlap: {overlap}")

 # Print ranked table
   print("\nRanked Table for List 1:")
   for i, (prec, rec) in enumerate(zip(precision1, recall1)):
        print(f"Rank {i + 1}: Precision = {prec:.2f}, Recall = {rec:.2f}")

   print("\nRanked Table for List 2:")
   for i, (prec, rec) in enumerate(zip(precision2, recall2)):
        print(f"Rank {i + 1}: Precision = {prec:.2f}, Recall = {rec:.2f}")
    
#GUI

root = Tk() # hoofdvenster
root.title("IR evaluator") # titelbalk
    
# bovenkant
label1 = Label(root, text="Search results 1:")
label2 = Label(root, text="Search results 2:")
label1.grid(row = 0, column = 0)
label2.grid(row = 0, column=1)

#textbox
set1 = Text(root, height = 10, width=50)
set2 = Text(root, height = 10, width=50)
set1.grid(row = 1, column = 0)
set2.grid(row = 1, column = 1)
set1.insert(END, "\n".join([f"{rel} - {text}" for rel, text in list1]))
set2.insert(END, "\n".join([f"{rel} - {text}" for rel, text in list2]))

#onderkant

label3 = Label(root, text="Total relevant documents: ")
label3.grid(row = 2, column =0, sticky = "E")
relevant_input = Entry(root)
relevant_input.grid(row = 2, column =1, sticky = "W")
relevant_input.insert(0, "15") #Voorbeeld

runQuery = Button(root, text="Run Query", command = calculate_metrics)
runQuery.grid(row = 3, column = 0, sticky = "E")

# Metrics display
metrics1_label = Label(root, text="")
metrics1_label.grid(row=4, column=0, columnspan=2, sticky="W")
metrics2_label = Label(root, text="")
metrics2_label.grid(row=5, column=0, columnspan=2, sticky="W")
overlap_label = Label(root, text="")
overlap_label.grid(row=6, column=0, columnspan=2, sticky="W")

root.mainloop()

