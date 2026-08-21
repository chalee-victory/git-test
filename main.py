prompts = [

    {
        "title": "에러 메시지 보는 지친 개발자",
        "content": "어두운 방 안, 늦은 밤 한 지친 한국인 개발자가 붉은 에러 메시지로 가득한 모니터를 바라보고 있는 모습, 드라마틱한 조명, 시네마틱, 포토리얼리스틱, 8K 해상도 --ar 16:9 --style raw",
        "category": "이미지 생성",
        "favorite": True
    },
    {
        "title": "감정형 불만 및 긴급 민원 테스트",
        "content": "민원인 정보: 김철수 / 50대 / 이사 당일 공과금 분쟁\n문의 사항: 오늘 서초구로 이사 왔는데, 이전 집주인이 수도요금을 안 내서 수도를 끊겠다고 합니다! 당장 오늘 저녁에 물을 써야 하는데 구청에서 당장 해결해 주세요!",
        "category": "자동화",
        "favorite": True
    },
    {
        "title": "정보 모호성 및 조건 복합 민원 테스트",
        "content": "민원인 정보: 박민지 / 40대 / 강남구에서 서초구로 이사 예정 (초등학생 4학년 자녀 동반)\n문의 사항: 이번에 이사 가는데 구청에 제출해야 할 서류랑 지원받을 수 있는 혜택 전부 알려주세요.",
        "category": "사무자동화",
        "favorite": True
    },

    {
        "title": "구청 민원 상담 AI 페르소나",
        "content": "너는 구청 민원실에서 근무하는 AI 상담 비서 '구청이'이다.\n민원인의 문의에 친절하고 정확하게 답변하는 것이 너의 임무이다.\n\n역할 수행 시 다음 원칙을 지켜라:\n1. 항상 존댓말과 공손한 어조를 사용한다.\n2. 민원인이 감정적으로 격앙되어 있어도 침착하게 응대한다.\n3. 정보가 불충분한 문의는 필요한 조건을 되물어 정확히 확인한다.\n4. 담당 부서 권한 밖의 요청(예: 즉시 취소, 예외 승인 등)은 처리할 수 없음을 안내하고, 올바른 절차나 담당 부서를 안내한다.\n5. 답변은 간결하되 필요한 정보(제출 서류, 절차, 연락처 등)를 빠뜨리지 않는다.",
        "category": "페르소나",
        "favorite": True
    }
]

categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

def show_menu():
    print("=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    print("선택 :")

def add_prompt(prompts):
    print("\n=== 프롬프트 추가 ===")

    # 1. 제목 입력받기 (빈칸이면 재입력 요청)
    title = input("제목(Enter=>종료): ")
    if title == "":
        print("\n제목이 비어있어 프롬프트 추가를 취소했습니다.")
        return

    # 2. 내용 입력받기 (빈칸이면 재입력 요청)
    content = input("내용: ")
    while content == "":
        print("내용은 비워둘 수 없습니다. 다시 입력해주세요.")
        content = input("내용: ")

    # 3. 카테고리 입력받기 (빈칸이면 재입력 요청)
    category = input("카테고리: ")
    while category == "":
        print("카테고리는 비워둘 수 없습니다. 다시 입력해주세요.")
        category = input("카테고리: ")

    # 4. 입력여부 확인하기(Y/N)
    chk = input("입력하시겟어요?(Y/N): ")
    if chk == 'N':
        print("\n프롬프트 추가를 취소했습니다.")
        return

    # 5. 새 딕셔너리 만들어서 prompts 리스트에 추가
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_prompt)

    print("\n프롬프트가 추가되었습니다!")

def show_list(prompts):
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    
    for i, prompt in enumerate(prompts, start=1):
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']} {star}")

    print(f"==총 {len(prompts)}개의 프롬프트==\n")

def show_by_category(prompts):
    print("\n=== 카테고리별 조회 ===")
    for i, cat in enumerate(categories, start=1):
        print(f"{i}) {cat}")
    choice = input("선택: ")
    selected = categories[int(choice) - 1]

    count = 0
    for i, prompt in enumerate(prompts, start=1):
        if prompt["category"] == selected:
            star = "⭐" if prompt["favorite"] else ""
            print(f"{i}. {prompt['title']} {star}")
            count += 1
    if count == 0:
        print("해당 프롬프트가 없습니다")
    else: 
        print(f"총{count}개의 프롬프트")


def search_prompt(prompts):
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ")
    
    print("\n검색 결과:")
    
    count = 0
    for i, prompt in enumerate(prompts, start=1):
        if keyword in prompt["title"] or keyword in prompt["content"]:
            star = "⭐" if prompt["favorite"] else ""
            print(f"{i}. [{prompt['category']}] {prompt['title']} {star}")
            count += 1
    
    if count == 0:
        print("검색 결과가 없습니다.")
    else:
        print(f"\n{count}개의 프롬프트를 찾았습니다.")

def show_detail(prompts):
    print("\n=== 프롬프트 상세 보기 ===")
    number = input("번호 입력: ")
    index = int(number) - 1
    prompt = prompts[index]
    
    star = "⭐" if prompt["favorite"] else ""
    
    print("─" * 30)
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {star}")
    print("─" * 30)
    print("내용:")
    print(prompt["content"])
    print("─" * 30)

def toggle_favorite(prompts):
    print("\n=== 즐겨찾기 관리 ===")
    number = input("프롬프트 번호 입력: ")
    index = int(number) - 1
    prompt = prompts[index]
    
    prompt["favorite"] = not prompt["favorite"]
    
    if prompt["favorite"]:
        print(f"\n'{prompt['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")
    else:
        print(f"\n'{prompt['title']}' 프롬프트를 즐겨찾기에서 해제했습니다.")

while True:
    show_menu()
    choice = input()

    if choice == "1":
        add_prompt(prompts)
    elif choice == "2":
        show_list(prompts)
    elif choice == "3":
        show_by_category(prompts)
    elif choice == "4":
        search_prompt(prompts)
    elif choice == "5":
        show_detail(prompts)
    elif choice == "6":
        toggle_favorite(prompts)
    elif choice == "7":
        print("777추후 구현 예정")
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("\n 잘못된 번호입니다. 다시 선택해 주세요.")

    