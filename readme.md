# LangChain AI Project Setup Guide

This guide provides step-by-step instructions to set up a Python project environment in VS Code for LangChain AI development. Follow these steps to ensure a smooth development experience.

---

## Prerequisites

1. Install **Python 3.8+** from [python.org](https://www.python.org/downloads/).
2. Install **Visual Studio Code** (VS Code) from [code.visualstudio.com](https://code.visualstudio.com/).
3. Install the **Python Extension for VS Code**:
   - Open VS Code.
   - Go to the Extensions view (`Ctrl+Shift+X`), and search for "Python".
   - Install the official Python extension by Microsoft.

---

## Steps to Set Up the Project

### 1. Create the Project Folder

1. Create a folder for your project, e.g., `langchain_project`.
2. Open this folder in VS Code: `File > Open Folder`.

---

### 2. Set Up a Virtual Environment

1. Open the terminal in VS Code: `Ctrl+`` (or `View > Terminal`).
2. Run the following command to create a virtual environment:
   bash
   python -m venv venv
   
3. Activate the virtual environment:
   - **Windows**:
     bash
     .\venv\Scripts\activate
    
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
4. Confirm the virtual environment is active:
   ```bash
   python --version
   ```

---

### 3. Install Required Libraries

1. Install LangChain and related dependencies:
   ```bash
   pip install langchain openai python-dotenv
   ```
2. Save the dependencies to a `requirements.txt` file:
   ```bash
   pip freeze > requirements.txt
   ```

---

### 4. Create a `.env` File for API Keys

1. In the project folder, create a file named `.env`.
2. Add your API keys to the `.env` file:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   OTHER_API_KEY=your_other_api_key_here
   ```
3. Add `.env` to your `.gitignore` to ensure it isn’t committed to version control:
   ```plaintext
   .env
   ```

---

### 5. Set Up VS Code Configuration

1. Create a `.vscode` folder in your project directory.
2. Inside `.vscode`, create a `settings.json` file.
3. Add the following content to `settings.json`:
   ```json
   {
       "python.pythonPath": "${workspaceFolder}/venv/bin/python",
       "python.envFile": "${workspaceFolder}/.env",
       "python.terminal.activateEnvironment": true
   }
   ```
   **Note for Windows**: Replace the Python path with:
   ```json
   "python.pythonPath": "${workspaceFolder}\\venv\\Scripts\\python.exe"
   ```

---

### 6. Test the Setup

1. Create a `main.py` file:
   ```python
   from langchain.prompts import PromptTemplate
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env
   load_dotenv()

   # Example usage of LangChain and environment variables
   api_key = os.getenv("OPENAI_API_KEY")
   prompt = PromptTemplate(
       input_variables=["name"],
       template="Hello, {name}! This is LangChain in action."
   )
   print(f"API Key: {api_key}")
   print(prompt.format(name="Anindita"))
   ```
2. Run the file:
   ```bash
   python main.py
   ```
   You should see your API key and a formatted prompt printed in the terminal.

---

### 7. Version Control (Optional)

1. Initialize Git:
   ```bash
   git init
   ```
2. Create a `.gitignore` file:
   ```plaintext
   venv/
   .env
   __pycache__/
   *.pyc
   *.pyo
   ```
3. Add and commit the changes:
   ```bash
   git add .
   git commit -m "Initial project setup"
   ```

---

## Final Directory Structure

Your project should now look like this:

```plaintext
langchain_project/
├── .vscode/
│   └── settings.json
├── venv/
├── main.py
├── .env
├── requirements.txt
├── .gitignore
```

You are now ready to start developing with LangChain!

---

### Troubleshooting

- If `.vscode` configurations don’t take effect, restart VS Code and reselect the Python interpreter (`Ctrl+Shift+P > Python: Select Interpreter`).
- Ensure your `.env` file is correctly formatted and stored in the root directory.

For further assistance, feel free to ask!

