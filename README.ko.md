# Nickname Maker
LLM 기반 영어 닉네임 추천 웹 서비스

[![Language](https://img.shields.io/badge/language-English-green.svg)](./README.md)


## 📌 프로젝트 개요
*   회사에서 영어 닉네임을 사용하는 직장인들을 위해, 입력된 정보를 기반으로 AI가 영어 닉네임을 추천해주는 웹사이트 기획 및 개발 
*   실제 서비스 배포를 통한 Docker 학습 목적

*   **개발기간**: 5 Days
*   **URL**: [View Website](http://13.238.182.199:8501/)

## ✨ 주요 기능
### 닉네임 추천
*   사용자 입력(이름, 성별, 나이, 원하는 분위기)을 기반으로 **LLM(GPT-4o-mini)**을 활용하여 최적의 영어 닉네임 추천

## 🛠 기술 스택

| Layer | Stacks |
| :--- | :--- |
| **Client** | Streamlit (Web UI) |
| **Server** | FastAPI, Docker, AWS EC2 |
| **CI/CD** | Github Actions |
| **LLM** | OpenAI GPT-4o-mini |

### UI 및 백엔드 API 서버
*   **Python 기반 Streamlit & FastAPI**: 
    *   **Streamlit**을 사용하여 빠르고 간편하게 웹 UI 구현
    *   추후 모바일(Flutter) 등 타 플랫폼으로의 서비스 확장을 고려하여 **FastAPI**로 백엔드 서버를 분리하여 구현

### 배포 및 인프라
*   **Docker & Docker Compose**: 
    *   Docker 이미지 기반으로 빌드 및 실행 환경을 구축하여 일관된 런타임 환경 유지
    *   Docker Compose를 통해 Streamlit UI와 FastAPI 서버를 독립된 컨테이너로 분리하여 효율적인 운영 환경 구축
*   **AWS EC2**: 클라우드 서버 호스팅
*   **GitHub Actions**: CI/CD 파이프라인을 통한 배포 자동화

## 🔍 트러블슈팅

### GitHub Actions에서 Docker로 EC2 배포 시 SSH 접속 실패
*   **에러 내용**: `2026/04/27 13:48:28 dial tcp ***:22: i/o timeout`
*   **원인 분석**: 
    *   SSH는 22번 포트를 사용하는데, 보안을 위해 인바운드 규칙을 특정 IP(내 컴퓨터)로만 제한
    *   GitHub Actions 워크플로우 실행 시마다 가상 환경의 IP가 변경되므로, 서버의 22번 포트가 이를 허용하지 않아 타임아웃 에러 발생
*   **해결 방법**: 
    *   **방법 1 (미선택)**: 22번 포트를 전체 개방(`0.0.0.0/0`) 하는 것은 보안상 권장되지 않음
    *   **방법 2 (선택)**: **AWS Systems Manager (SSM)** 사용. 22번 포트를 개방하지 않고도 보안 인증을 통해 EC2 인스턴스에 안전하게 접근하여 해결

### AWS SSM 설정 과정 중 Git 권한 및 환경 변수 문제
*   **에러 내용**: `fatal: detected dubious ownership in repository at '/home/ubuntu/nickname_maker'`
*   **원인 분석**: 
    1.  **Dubious Ownership**: Git 보안 업데이트로 인해 명령 실행자(`ssm-user`)와 폴더 소유자(`ubuntu`)가 다를 경우 신뢰할 수 없는 디렉토리로 간주
    2.  **$HOME 변수 미지정**: SSM 명령 실행 시 환경 변수가 로드되지 않아 Git이 설정 파일(`.gitconfig`) 위치를 찾지 못함
*   **해결 방법**: 
    *   홈 디렉토리를 강제로 지정하고, `sudo -u ubuntu -i bash -c` 명령어를 통해 `ubuntu` 사용자의 권한으로 명령어를 실행하도록 수정
    ```bash
    "export HOME=/home/ubuntu",
    "sudo -u ubuntu -i bash -c \"cd /home/ubuntu/nickname_maker && ...\""
    ```

## 📈 프로젝트 성과
*   **GitHub Actions 기반 CI/CD 구축**: Docker 기반 웹 애플리케이션을 AWS EC2에 자동 배포하는 파이프라인 완성
*   **멀티 컨테이너 운영**: Docker Compose를 활용하여 복수 서비스(Streamlit, FastAPI)의 컨테이너화 및 운영 자동화 실습
*   **보안 강화**: SSH 방식의 네트워크 이슈를 해결하고 **SSM 기반 인증 방식**을 도입하여 보안성 향상