
import os
import psycopg2
from psycopg2 import sql

# --- [DB 설정] ---
# 사용자 환경에 맞게 DB 연결 정보를 수정하세요.
# 환경 변수 사용을 권장합니다. 예: os.environ.get('DB_HOST', 'localhost')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'study_db')
DB_USER = os.environ.get('DB_USER', 'your_user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'your_password')

def get_db_connection():
    """데이터베이스 연결을 생성하고 반환합니다."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"DB 연결에 실패했습니다: {e}")
        print("DB 연결 정보를 확인하거나 PostgreSQL 서버가 실행 중인지 확인하세요.")
        return None

# --- [📌 문제 1 — 테이블 생성 함수] ---
def create_books_table():
    ""'books' 테이블을 생성합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cur:
            # UUID 생성을 위한 확장 활성화
            cur.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
            
            # 기존 테이블이 있다면 삭제
            cur.execute("DROP TABLE IF EXISTS books;")

            # 새 테이블 생성
            cur.execute("""
                CREATE TABLE books (
                    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                    title VARCHAR(100) NOT NULL,
                    price INT NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()
            print("books 테이블이 생성되었습니다.")
    except psycopg2.Error as e:
        print(f"테이블 생성 중 오류 발생: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()

# --- [📌 문제 2 — INSERT 함수] ---
def insert_books():
    ""'books' 테이블에 3개의 테스트 데이터를 삽입합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    books_to_insert = [
        ('파이썬 입문', 19000),
        ('알고리즘 기초', 25000),
        ('네트워크 이해', 30000)
    ]

    try:
        with conn.cursor() as cur:
            insert_query = "INSERT INTO books (title, price) VALUES (%s, %s);"
            # executemany를 사용하여 여러 데이터를 한 번에 삽입
            psycopg2.extras.execute_batch(cur, insert_query, books_to_insert)
            
            conn.commit()
            print(f"{len(books_to_insert)}개 도서가 삽입되었습니다.")
    except psycopg2.Error as e:
        print(f"데이터 삽입 중 오류 발생: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()

# --- [📌 문제 3 — SELECT 함수] ---
def get_all_books():
    ""모든 도서 정보를 조회하고 출력합니다."""
    conn = get_db_connection()
    if conn is None:
        return
        
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, price FROM books ORDER BY created_at;")
            books = cur.fetchall()
            print("\n--- [전체 도서 목록] ---")
            if not books:
                print("데이터가 없습니다.")
            for book in books:
                print(f"ID: {book[0]}, 제목: {book[1]}, 가격: {book[2]:,}원")
            print("----------------------")
    except psycopg2.Error as e:
        print(f"데이터 조회 중 오류 발생: {e}")
    finally:
        if conn:
            conn.close()

def get_expensive_books():
    ""가격이 25000원 이상인 도서를 조회하고 출력합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, price FROM books WHERE price >= 25000 ORDER BY price DESC;")
            books = cur.fetchall()
            print("\n--- [가격이 25,000원 이상인 도서] ---")
            if not books:
                print("해당 조건의 도서가 없습니다.")
            for book in books:
                print(f"ID: {book[0]}, 제목: {book[1]}, 가격: {book[2]:,}원")
            print("-----------------------------------")
    except psycopg2.Error as e:
        print(f"데이터 조회 중 오류 발생: {e}")
    finally:
        if conn:
            conn.close()

def get_book_by_title(title: str):
    ""주어진 제목으로 도서를 조회하고 출력합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, price FROM books WHERE title = %s;", (title,))
            book = cur.fetchone()
            print(f"\n--- ['{title}' 도서 검색 결과] ---")
            if book:
                print(f"ID: {book[0]}, 제목: {book[1]}, 가격: {book[2]:,}원")
            else:
                print(f"'{title}' 제목의 도서를 찾을 수 없습니다.")
            print("---------------------------------")
    except psycopg2.Error as e:
        print(f"데이터 조회 중 오류 발생: {e}")
    finally:
        if conn:
            conn.close()

# --- [📌 문제 4 — UPDATE 함수] ---
def update_second_book_price():
    "''알고리즘 기초' 도서의 가격을 27000으로 변경합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    target_title = '알고리즘 기초'
    new_price = 27000

    try:
        with conn.cursor() as cur:
            # 1. UUID를 SELECT로 가져오기
            cur.execute("SELECT id FROM books WHERE title = %s;", (target_title,))
            book_id_result = cur.fetchone()
            
            if not book_id_result:
                print(f"'{target_title}' 도서를 찾을 수 없어 업데이트할 수 없습니다.")
                return

            book_id = book_id_result[0]

            # 2. 가져온 UUID를 사용하여 가격 업데이트
            cur.execute("UPDATE books SET price = %s WHERE id = %s;", (new_price, book_id))
            conn.commit()
            
            if cur.rowcount > 0:
                print(f"'{target_title}' 도서 가격이 {new_price:,}원으로 수정되었습니다.")
            else:
                print("가격 업데이트에 실패했습니다.")

    except psycopg2.Error as e:
        print(f"업데이트 중 오류 발생: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()

# --- [📌 문제 5 — DELETE 함수] ---
def delete_third_book():
    "''네트워크 이해' 도서를 삭제합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    target_title = '네트워크 이해'

    try:
        with conn.cursor() as cur:
            # 1. UUID를 SELECT로 가져오기
            cur.execute("SELECT id FROM books WHERE title = %s;", (target_title,))
            book_id_result = cur.fetchone()

            if not book_id_result:
                print(f"'{target_title}' 도서를 찾을 수 없어 삭제할 수 없습니다.")
                return

            book_id = book_id_result[0]

            # 2. 가져온 UUID를 사용하여 데이터 삭제
            cur.execute("DELETE FROM books WHERE id = %s;", (book_id,))
            conn.commit()
            
            if cur.rowcount > 0:
                print(f"'{target_title}' 도서가 삭제되었습니다.")
            else:
                print("삭제에 실패했습니다.")

    except psycopg2.Error as e:
        print(f"삭제 중 오류 발생: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()


# --- [메인 실행 로직] ---
if __name__ == '__main__':
    print("--- PostgreSQL CRUD 작업을 시작합니다. ---")

    # 1. 테이블 생성 (기존 테이블이 있다면 삭제 후 재생성)
    create_books_table()

    # 2. 데이터 삽입
    insert_books()

    # 3. 데이터 조회
    get_all_books()
    get_expensive_books()
    get_book_by_title('파이썬 입문')
    get_book_by_title('없는 책')

    # 4. 데이터 수정
    update_second_book_price()
    print("\n... 가격 수정 후 데이터 확인 ...")
    get_all_books()

    # 5. 데이터 삭제
    delete_third_book()
    print("\n... 도서 삭제 후 데이터 확인 ...")
    get_all_books()
    
    print("\n--- 모든 작업이 완료되었습니다. ---")
