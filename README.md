# StudyBuddy AI

**StudyBuddy AI** is an AI-powered personal assistant designed to help students manage tasks, track deadlines, and receive personalized study recommendations. With integration to Google Calendar, task visualization, and machine learning for prioritization, StudyBuddy AI provides an efficient way to stay organized and productive.

---

## **Features**

### Task Management
- Add, delete, and view tasks with deadlines and importance levels.
- Automatically save and load tasks.

### Personalized Recommendations
- Science-based suggestions tailored to task urgency and importance.
- Encourages effective techniques like time blocking, the Pomodoro method, and spaced repetition.

### Google Calendar Integration
- Sync tasks automatically with your Google Calendar for better scheduling.

### Task Visualization
- Horizontal bar charts displaying deadlines.
- Importance and due dates printed in the middle of each bar.

### Task Prioritization
- Machine learning prioritizes tasks based on urgency and importance.

---

## **How to Use**

### 1. **Installation**
- Clone this repository:
git clone https://github.com/cjfort/StudyBuddyAI.git 
cd StudyBuddyAI

- Install the required dependencies:
pip install -r requirements.txt

---

### 2. **Google Calendar Setup**

Follow these steps to set up the Google Calendar API for your project.

---

#### **1. Create a Google Cloud Project**
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Log in with your Google account.
3. Click the **Select a Project** dropdown in the top navigation bar.
4. Click **New Project**.
5. Enter a name for your project (e.g., "StudyBuddyAI").
6. Click **Create** and wait for the project to be created.

---

#### **2. Enable the Google Calendar API**
1. Once your project is created, go to the **APIs & Services > Library** in the left-hand menu.
2. In the search bar, type **Google Calendar API**.
3. Click on the **Google Calendar API** result.
4. Click **Enable** to activate the API for your project.

---

#### **3. Configure the OAuth Consent Screen**
1. Go to **APIs & Services > OAuth Consent Screen**.
2. Choose **External** for the user type and click **Create**.
3. Fill in the required fields:
   - **App Name**: (e.g., "StudyBuddyAI").
   - **User Support Email**: Your email address.
   - **Developer Contact Information**: Your email address.
4. Click **Save and Continue**.
5. Skip the scopes configuration by clicking **Save and Continue**.
6. Add test users:
   - Enter your email address under the **Test Users** section.
   - Click **Add** and then **Save and Continue**.

---

#### **4. Create OAuth Credentials**
1. Go to **APIs & Services > Credentials**.
2. Click **Create Credentials** > **OAuth Client ID**.
3. Under **Application Type**, select **Desktop App**.
4. Enter a name for your credentials (e.g., "StudyBuddyAI Credentials").
5. Click **Create**.
6. Click **Download JSON** to download your credentials file.
   - The file will be named `credentials.json`.
   - Place this file in the root directory of your project.

---

### 3. **Run the Application**
Start the application using:

python main.py

---

### 4. **Using StudyBuddy AI**
- **Add Tasks**: Enter the task name, deadline, and importance level (1-5).
- **Get Recommendations**: Click the "Get Recommendations" button for personalized study tips.
- **Visualize Tasks**: Use the "Visualize Tasks" button to view deadlines on a bar chart.
- **Sync to Calendar**: Tasks are automatically added to your Google Calendar.

---

## **Project Structure**
StudyBuddyAI/
│
├── main.py                   # Entry point of the application
├── task_manager.py           # Handles task-related functionalities
├── recommendation_engine.py  # Provides personalized study recommendations
├── data_manager.py           # Manages task storage and retrieval
├── calendar_integration.py   # Integrates Google Calendar
├── ml_prioritizer.py         # Machine learning for task prioritization
├── ui.py                     # Graphical user interface
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

---

## **Technologies Used**
### Programming
- **Python**: Core programming language.
- **Tkinter**: For the graphical user interface.
- **Matplotlib**: For visualizing tasks.
### APIs
- **Google Calendar API**: Integrates tasks with your Google Calendar.
### Machine Learning
- **scikit-learn**: Used for task prioritization based on urgency and importance.

---

## **Key Algorithms and Techniques**
### Science-Based Recommendations
- High Urgency: Focused, distraction-free work strategies like time blocking.
- Medium Urgency: Strategic scheduling and milestones to maintain progress.
- Low Urgency: Incremental progress and spaced repetition to avoid procrastination.
### Visualization
- Dynamic horizontal bar charts with importance and deadlines displayed inside each bar.
- Machine Learning Prioritization
- Decision tree classifier trained to predict task priority based on urgency (days to deadline) and importance level.

---

## **Author**
This project was created by **Cooper Fort**.

---

## **Future Enhancements**
- Notifications and reminders for tasks.
- Advanced analytics on productivity.
- Mobile app integration for on-the-go task management.

---

## **License**
This project is licensed under the MIT License.