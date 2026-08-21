# 개발환경 설정 및 Git 로그 확인 — VS Code 터미널 캡처

> `CLI_프롬프트.pdf` 캡처 화면을 텍스트로 정리한 문서입니다.
> VS Code 통합 터미널에서 개발 환경 정보와 Git 커밋 히스토리를 함께 확인하였습니다.

---

## 1. 개발 환경 정보 확인

```powershell
PS C:\git-test> python --version
>> git --version
>> git config --global user.name
>> git config --global user.email
Python 3.12.9
git version 2.55.0.windows.3
에펠
chalee6110@gmail.com
```

| 항목 | 값 |
|---|---|
| Python 버전 | 3.12.9 |
| Git 버전 | 2.55.0.windows.3 |
| Git 사용자 이름 | 에펠 |
| Git 사용자 이메일 | chalee6110@gmail.com |

---

## 2. Git 커밋 히스토리 그래프 확인

```powershell
PS C:\git-test> git log --oneline --graph
* f8cccf7 (HEAD -> main, origin/main, origin/HEAD) Update readme with project description
* 8a40386 docs: write README with program description and usage
* e89811e fix: add exception handling for invalid number input
* 1135086 fix: add exception handling for invalid number input
* fad6420 feat: implement show_favorites function
* 6a0f3ff feat: implement toggle_favorite function
* 7025874 feat: implement show_detail function
* 2d3b2d9 feat: implement search_prompt function
* 4da7eb3 feat: implement show_by_category function
* 23cb755 (feature/list) feat: implement show_list function
* f1685f9 feat: implement add_prompt function
* b23c829 feat: add base prompt data and menu skeleton
* dca795b chore: init project with README
```

**총 커밋 수: 13개** (요구사항: 최소 10개 이상 → 충족)

---

## 3. 확인 환경

- **에디터**: Visual Studio Code
- **터미널**: PowerShell (VS Code 통합 터미널)
- **작업 폴더**: `C:\git-test`
- **현재 브랜치**: `main` (하단 상태 표시줄에서 `main*` 확인)
- **GitHub 저장소**: `chalee-victory/git-test`

---

## 4. 제출물 대응

이 캡처 하나로 아래 제출 요건 두 가지를 충족합니다.

| 제출물 항목 | 충족 여부 |
|---|---|
| 개발환경 설정 스크린샷 (VSCode, Python 버전, Git 설정) | ✅ |
| `git log --oneline --graph` 결과 스크린샷 | ✅ |
