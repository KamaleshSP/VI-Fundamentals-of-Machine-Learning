from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Font
        self.set_font('Arial', 'B', 12)
        # Content
        self.cell(0, 10, 'Kamalesh S P | 230701138 | FOML Activity 1', 0, 1, 'R')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 8, body)
        self.ln()

    def add_section(self, title, body):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 6, body)
        self.ln(3)

pdf = PDF()
pdf.add_page()

# Title
pdf.set_font('Arial', 'B', 20)
pdf.cell(0, 20, 'Case Study: Components of Learning', 0, 1, 'C')
pdf.ln(10)

# Intro
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 8, "Machine Learning involves a computer program learning from experience (E) with respect to some class of tasks (T) and performance measure (P). This document explores the specific components of learning required to build systems for three distinct use cases.")
pdf.ln(10)

# --- Use Case 1 ---
pdf.chapter_title('1. Predicting Placement Chances')

pdf.add_section('Problem Definition', 
"The goal is to build a predictive model that analyzes a student's academic and non-academic profile to estimate the probability of them getting placed in a company.")

pdf.add_section('The Task (T)', 
"Nature: Supervised Learning (Classification/Regression).\nDefinition: Map input variables (profile) to output (Placement Status).\nOutput: Binary label (0/1) or probability score.")

pdf.add_section('The Experience / Data (E)', 
"Input Features (X):\n- Academic: CGPA, 10th/12th Marks, Arrears.\n- Technical: Skills (React, Node.js), Project scores.\n- Demographics: Department.\nTarget Labels (Y): Actual placement status of previous batches.")

pdf.add_section('Performance Measure (P)', 
"- Accuracy: Percentage of correct predictions.\n- Precision & Recall: To minimize false positives.\n- Confusion Matrix: To visualize classification errors.")

pdf.add_section('Learning Algorithm', 
"- Logistic Regression: For binary classification.\n- Random Forest: For handling non-linear data patterns.")

pdf.ln(5)

# --- Use Case 2 ---
pdf.chapter_title('2. Detecting Fake Reviews')

pdf.add_section('Problem Definition', 
"The objective is to identify whether a product review posted on an e-commerce platform is genuine or fake (spam/bot-generated).")

pdf.add_section('The Task (T)', 
"Nature: Supervised Learning (NLP).\nDefinition: Classify text into 'Fake' or 'Genuine'.")

pdf.add_section('The Experience / Data (E)', 
"Input Features (X):\n- Textual: Bag-of-words, sentiment score.\n- Metadata: Timestamp, account age.\n- Behavioral: Rating deviation.\nTarget Labels (Y): Moderator-flagged reviews.")

pdf.add_section('Performance Measure (P)', 
"- F1-Score: Best for imbalanced data (mostly real reviews).\n- ROC-AUC: Measures separation capability.")

pdf.add_section('Learning Algorithm', 
"- Naive Bayes: Probabilistic classifier for text.\n- RNNs/LSTMs: Deep learning for context analysis.")

pdf.ln(5)

# --- Use Case 3 ---
pdf.add_page() # New page for the last topic if needed
pdf.chapter_title('3. Predicting Electricity Consumption')

pdf.add_section('Problem Definition', 
"Forecast future electricity consumption based on historical usage and external factors.")

pdf.add_section('The Task (T)', 
"Nature: Regression / Time Series Forecasting.\nDefinition: Predict a continuous numerical value (kWh).")

pdf.add_section('The Experience / Data (E)', 
"Input Features (X):\n- Historical Usage: Previous kWh logs.\n- Temporal: Hour, Day, Seasonality.\n- External: Temperature, Holidays.\nTarget Labels (Y): Future consumption values.")

pdf.add_section('Performance Measure (P)', 
"- MAE (Mean Absolute Error): Average prediction error.\n- RMSE (Root Mean Squared Error): Penalizes large errors.")

pdf.add_section('Learning Algorithm', 
"- Linear Regression: For simple trends.\n- ARIMA: Statistical time-series model.\n- LSTM: Neural network for sequential patterns.")

# Output
pdf.output("138_FOML_Activity_Kamalesh.pdf")
print("PDF Generated Successfully")