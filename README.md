# PyQt5
# PyQt5
# **OpenModelica Runner**  

## **📌 Project Description**  
**OpenModelica Runner** is a **PyQt5-based GUI application** designed to simplify running Modelica simulations.  
This tool allows users to **select an OpenModelica executable, set simulation parameters, and execute the simulation** without needing to use the command line.  

### **Key Functionalities:**  
✔ **Browse & Select Modelica Executable**  
✔ **Set Simulation Start & Stop Times**  
✔ **Execute Modelica Simulations with One Click**  
✔ **View Real-Time Logs in GUI**  
✔ **Error Handling for Invalid Inputs**  
✔ **Multithreading Support for UI Responsiveness**  

---

## **📥 Installation & Setup**  

### **1️⃣ Prerequisites**  
Ensure you have the following installed:  
- **Python 3.x**  
  Check by running:  
  ```bash
  python3 --version

  2️⃣ Clone the Repository
Open a terminal or command prompt.
Run the following commands:
bash
Copy
Edit
git clone https://github.com/your-username/OpenModelica-Runner.git
cd OpenModelica-Runner
3️⃣ Install Dependencies
Inside the project folder, install the required dependencies:

bash
Copy
Edit
pip install PyQt5
🚀 Steps to Use the Application
1️⃣ Run the Application
Execute the following command:

bash
Copy
Edit
python your_script.py
(Replace your_script.py with your actual filename.)

2️⃣ Select Modelica Executable
Click "Browse..." to select the OpenModelica executable (.exe file).
3️⃣ Enter Simulation Parameters
Input Start Time (s) and Stop Time (s).
4️⃣ Run the Simulation
Click "Run Simulation" to start the process.
The console output will display real-time logs.
A message box will confirm if the simulation succeeded or failed.
📸 Example Screenshot
(You can add a screenshot here by uploading an image to your GitHub repository and linking it.)

🛠️ How It Works (Methodology)
1️⃣ The application executes the Modelica simulation using Python’s subprocess.Popen().
2️⃣ Multithreading (QThread) ensures that the UI remains responsive while the simulation runs.
3️⃣ Real-time logs from the Modelica process are displayed inside the GUI.
4️⃣ Input validation ensures:

A valid executable file is selected.
Start time is less than stop time.
Only numeric values are entered.
5️⃣ Error messages provide feedback if something goes wrong.
📁 Project Structure
bash
Copy
Edit
/OpenModelica-Runner
│── main.py         # Main Python script (GUI application)
│── README.md              # Project documentation



