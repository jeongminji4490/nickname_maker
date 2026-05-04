# Nickname Maker
LLM-based Nickname Recommendation Web Service

[![Language](https://img.shields.io/badge/language-Korean-blue.svg)](./README.ko.md)

## 📌 Project Overview
*   Planned and Developed a web service that AI recommends a personalized english nickname based on the user inputs for workers who are using an english nickname in the company
*   Learning Docker through actual sevice deployment

## ✨ Key Features
### Nickname Recommendation
*   Provides personalized English nickname recommendations using **LLM (GPT-4o-mini)** based on user inputs such as Name, Gender, Age, and Desired Vibe.

## 🛠 Tech Stack
### UI & Backend API Server
*   Developed using **Python-based Streamlit and FastAPI**.
*   Used **Streamlit** for rapid and easy Web UI development.
*   Implemented the backend with **FastAPI** considering future service expansion to other platforms (e.g., Flutter).

### Deployment & Infrastructure
*   **Docker & Docker Compose**: 
    *   Containerized the web application to provide a consistent runtime environment without additional package installations or local setup.
    *   Used Docker Compose to decouple the Streamlit UI and FastAPI server into independent containers for efficient testing and management.
*   **AWS EC2**: Primary server hosting.
*   **GitHub Actions**: Automated CI/CD pipeline for seamless deployment.

## 🔍 Troubleshooting

### 🚨 GitHub Actions SSH Connection Timeout to EC2
*   **Error**: `2026/04/27 13:48:28 dial tcp ***:22: i/o timeout`
*   **Cause**: 
    *   The SSH protocol uses Port 22 by default.
    *   The Security Group was configured to allow Port 22 only for my local IP address.
    *   Since GitHub Actions runners use dynamic IP addresses that change with every workflow execution, the server blocked the connection.
*   **Resolution**: 
    *   **Option 1**: Opening Port 22 to all IPs (`0.0.0.0/0`). (Rejected due to security risks).
    *   **Option 2 (Selected)**: **AWS Systems Manager (SSM)**. This allowed secure access to the EC2 instance without exposing Port 22 to the public.

### 🚨 AWS SSM "Dubious Ownership" & $HOME Variable Issues
*   **Issue**: Encountered `fatal: detected dubious ownership in repository` during SSM execution.
*   **Cause**: 
    1.  **Dubious Ownership**: Due to Git security updates, Git blocks access if the user running the command (usually `root` or `ssm-user` in SSM) differs from the directory owner (`ubuntu`).
    2.  **Missing $HOME**: Environment variables often fail to load during SSM commands, causing Git to fail because it cannot locate the `.gitconfig` file (which requires `$HOME`).
*   **Resolution**: 
    *   Manually specified the home directory and executed commands as the `ubuntu` user using `sudo -u ubuntu -i bash -c`.
    ```bash
    "export HOME=/home/ubuntu",
    "sudo -u ubuntu -i bash -c \"cd /home/ubuntu/nickname_maker && ...\""
    ```

## 📈 Project Achievements
*   Established a **GitHub Actions-based CI/CD pipeline** to automate the deployment of Dockerized applications to AWS EC2.
*   Containerized and automated the operation of multi-services (Streamlit, FastAPI) using **Docker Compose**.
*   Enhanced security by adopting **SSM-based authentication**, resolving network issues associated with traditional SSH methods.