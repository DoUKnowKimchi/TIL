# 181218 Day2

## 1. git (버전 관리 시스템)

- made by Linux Torvalds => 영상한번 보기.

- 코드의 History 를 관리하며 개발된 과정과 역사를 볼 수 있음.

- 프로젝트 이전 버전을 복원하고 변경 사항을 비교, 분석 및 병합도 가능.
- DVCS (Distribute Version Control System)

git init : 깃 디렉토리 실정

git status : 상태확인



### 깃의 작업 흐름

**작업할 파일** => `add` => **커밋할 목록** => `commit` => **쌓인 커밋** => `push` => **github**

*working directory*         *index(staging area)*                     *head*

`git add` 커밋할 목록에추가

`commit` 커밋(Create a snapshot) 만들기

`push` 현재까지의 역사 ( commits)가 기록되어 있는 곳에 새로 생성한 커밋을 만들기.

`diff` git 변한 내용 확인

`log` 커밋 히스토리 조회

`checkout`  스냅샷을 활용하여 이동

``git remote add origin https://github.com/DoUKnowKimchi/TIL.git` 원격 저장소 저장



