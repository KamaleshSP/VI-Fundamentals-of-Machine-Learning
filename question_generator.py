# This script generates a ready-to-download PDF in the exact lab-record format requested

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4

file_path = "FOML lab 1b.pdf"

doc = SimpleDocTemplate(file_path, pagesize=A4)
styles = getSampleStyleSheet()

title_style = styles["Title"]
heading_style = styles["Heading2"]
body_style = styles["BodyText"]
code_style = ParagraphStyle(
    'CodeStyle',
    fontName='Courier',
    fontSize=9,
    leading=12
)

story = []

story.append(Paragraph("A PYTHON PROGRAM TO IMPLEMENT UNIVARIATE, BIVARIATE AND MULTIVARIATE REGRESSION", title_style))
story.append(Spacer(1, 12))

story.append(Paragraph("<b>Aim:</b>", heading_style))
story.append(Paragraph(
    "To implement a Python program using univariate, bivariate and multivariate regression features "
    "for a given Iris dataset.", body_style))

story.append(Spacer(1, 10))
story.append(Paragraph("<b>Algorithm:</b>", heading_style))

algorithm_text = """
Step 1: Import necessary libraries:
• pandas for data manipulation,
• numpy for numerical operations, and
• matplotlib.pyplot for plotting.

Step 2: Read the dataset:
• Load the Iris dataset.
• Store the dataset in a DataFrame.

Step 3: Prepare the data:
• Extract independent variables (X) and dependent variable (y).
• Reshape the data if required.

Step 4: Univariate Regression:
• Use one independent variable.
• Fit a Linear Regression model.
• Predict values and calculate R-squared.

Step 5: Bivariate Regression:
• Use two independent variables.
• Fit a Linear Regression model.
• Predict values and calculate R-squared.

Step 6: Multivariate Regression:
• Use more than two independent variables.
• Fit a Linear Regression model.
• Predict values and calculate R-squared.

Step 7: Plot the results:
• Scatter plot with regression line for univariate.
• 3D scatter plot for bivariate.
• Actual vs predicted plot for multivariate.

Step 8: Display the results:
• Print coefficients, intercepts, and R-squared values.
"""

story.append(Preformatted(algorithm_text, body_style))

story.append(Spacer(1, 10))
story.append(Paragraph("<b>PROGRAM:</b>", heading_style))

program_code = """ """

story.append(Preformatted(program_code, code_style))

story.append(Spacer(1, 10))
story.append(Paragraph("<b>RESULT:</b>", heading_style))
story.append(Paragraph(
    "Thus, the Python program to implement univariate, bivariate and multivariate regression "
    "for the given Iris dataset was successfully executed and the features were analyzed "
    "using appropriate plots.", body_style))

doc.build(story)

file_path
