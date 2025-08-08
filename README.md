📄 PDF Merger
A simple Python script to merge multiple PDF files into a single document. This project is a straightforward and efficient tool for combining PDF files directly from the command line.

✨ Features
✅ Merges multiple PDF files into one.

🚀 Simple command-line interface.

💻 Easy-to-understand codebase using the PyPDF2 library.

🛠️ Prerequisites
Before you begin, ensure you have the following installed on your system:

🐍 Python 3.6 or higher

📦 pip (Python package installer)

🚀 Installation
Follow these steps to get your project up and running:

Clone the repository:
git clone https://github.com/your-username/pdf-merger.git
cd pdf-merger

Create a virtual environment (recommended):

python -m venv venv

On Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install the required dependencies:

pip install PyPDF2

🏃 Usage
To merge PDF files, place the files you want to merge in the same directory as the script.

To merge files file1.pdf and file2.pdf into merged.pdf:

python pdf_merger.py --output merged.pdf file1.pdf file2.pdf

You can add as many files as you like:

python pdf_merger.py --output final_document.pdf file1.pdf file2.pdf file3.pdf

To get help with the command-line arguments:

python pdf_merger.py --help

📦 Dependencies
PyPDF2: A free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
