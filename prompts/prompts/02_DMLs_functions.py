import psycopg2
from psycopg2 import sql
import os
from pprint import pprint

# ----------------------------------------------------------------------
# [필수 수정] PostgreSQL 연결 설정 정보
# ----------------------------------------------------------------------
# 이 값들을 실제 PostgreSQL 환경에 맞게 수정해야 합니다.
DB_NAME = os.environ.get("POSTGRES_DB", "mydb")
DB_USER = os.environ.get("POSTGRES_USER", "postgres")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "mypassword")
DB_HOST = os.environ.get("POSTGRES_HOST", "localhost")
DB_PORT = os.environ.get("POSTGRES_PORT", "5432")

# ----------------------------------------------------------------------
# 데이터베이스 연결 관리 함수
# ----------------------------------------------------------------------

def get_connection():
    """데이터베이스 연결 객체를 반환합니다."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"PostgreSQL 연결 오류 발생: {e}")
        print("-> [주의] 연결 정보를 확인하거나 PostgreSQL 서버가 실행 중인지 확인하세요.")
        return None

# ----------------------------------------------------------------------
# 📌 문제 1: 테이블 생성 함수 구현 (create_books_table)
# ----------------------------------------------------------------------

def create_books_table():
    """
    요구사항에 맞춰 'books' 테이블을 생성합니다.
    - id: UUID PRIMARY KEY DEFAULT uuid_generate_v4()
    - title: VARCHAR(100)
    - price: INT
    """
    conn = get_connection()
    if not conn: return

    try:
        with conn.cursor() as cur:
            # UUID-OSSP 확장 기능 활성화 (없을 경우에만 생성)
            cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
            # 기존 테이블이 있다면 삭제 (테스트 환경의 편의를 위해)
            cur.execute("DROP TABLE IF EXISTS books CASCADE;")
            
            # 테이블 생성 쿼리 (요구사항에 명시된 uuid_generate_v4 사용)
            create_table_query = """
            CREATE TABLE books (
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                title VARCHAR(100) NOT NULL,
                price INT NOT NULL
            );
            """
            cur.execute(create_table_query)
            conn.commit()
            print("✨ 'books' 테이블이 성공적으로 생성되었습니다.")
            
    except psycopg2.Error as e:
        print(f"테이블 생성 오류: {e}")
        conn.rollback()
    finally:
        if conn: conn.close()

# ----------------------------------------------------------------------
# 📌 문제 2: INSERT 함수 구현 (insert_books)
# ----------------------------------------------------------------------

def insert_books():
    """테스트용 도서 데이터를 books 테이블에 삽입합니다."""
    conn = get_connection()
    if not conn: return

    books_data = [
        ("파이썬 입문", 19000),
        ("알고리즘 기초", 25000),
        ("네트워크 이해", 30000)
    ]
    
    try:
        with conn.cursor() as cur:
            insert_query = "INSERT INTO books (title, price) VALUES (%s, %s);"
            cur.executemany(insert_query, books_data)
            conn.commit()
            print(f"✨ {len(books_data)}개 도서가 성공적으로 삽입되었습니다.")
            
    except psycopg2.Error as e:
        print(f"데이터 삽입 오류: {e}")
        conn.rollback()
    finally:
        if conn: conn.close()

# ----------------------------------------------------------------------
# 📌 문제 3: SELECT 함수 구현 (전체, 가격별, 제목별 조회)
# ----------------------------------------------------------------------

def get_all_books():
    """전체 도서 데이터를 조회하여 반환합니다."""
    conn = get_connection()
    if not conn: return []
    
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, price FROM books ORDER BY price ASC;")
            return cur.fetchall()
            
    except psycopg2.Error as e:
        print(f"전체 조회 오류: {e}")
        return []
    finally:
        if conn: conn.close()

def get_expensive_books():
    """가격이 25000원 이상인 도서 데이터를 조회하여 반환합니다."""
    conn = get_connection()
    if not conn: return []
    
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, price FROM books WHERE price >= 25000 ORDER BY price DESC;")
            return cur.fetchall()
            
    except psycopg2.Error as e:
        print(f"고가 도서 조회 오류: {e}")
        return []
    finally:
        if conn: conn.close()

def get_book_by_title(title):
    """title이 일치하는 도서 데이터를 조회하여 반환합니다."""
    conn = get_connection()
    if not conn: return None
    
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, price FROM books WHERE title = %s;", (title,))
            return cur.fetchone()
            
    except psycopg2.Error as e:
        print(f"제목별 조회 오류: {e}")
        return None
    finally:
        if conn: conn.close()

# ----------------------------------------------------------------------
# 📌 문제 4: UPDATE 함수 구현 (update_second_book_price)
# ----------------------------------------------------------------------

def update_book_price_by_title(title, new_price):
    """주어진 제목의 도서 가격을 수정합니다."""
    conn = get_connection()
    if not conn: return
    
    try:
        with conn.cursor() as cur:
            # 1. SELECT로 UUID 조회
            cur.execute("SELECT id FROM books WHERE title = %s;", (title,))
            result = cur.fetchone()
            if not result:
                print(f"오류: 제목 '{title}'에 해당하는 도서를 찾을 수 없습니다.")
                return

            book_uuid = result[0]

            # 2. UPDATE 수행
            cur.execute("UPDATE books SET price = %s WHERE id = %s;", (new_price, book_uuid))
            conn.commit()
            
            if cur.rowcount > 0:
                print(f"✨ '{title}' 도서 가격이 {new_price:,}원으로 수정되었습니다.")
            else:
                print(f"'{title}' 도서 가격 수정에 실패했습니다.")
                
    except psycopg2.Error as e:
        print(f"업데이트 오류: {e}")
        conn.rollback()
    finally:
        if conn: conn.close()

# ----------------------------------------------------------------------
# 📌 문제 5: DELETE 함수 구현 (delete_book_by_title)
# ----------------------------------------------------------------------

def delete_book_by_title(title):
    """주어진 제목의 도서를 삭제합니다."""
    conn = get_connection()
    if not conn: return

    try:
        with conn.cursor() as cur:
            # 1. SELECT로 UUID 조회
            cur.execute("SELECT id FROM books WHERE title = %s;", (title,))
            result = cur.fetchone()
            if not result:
                print(f"오류: 제목 '{title}'에 해당하는 도서를 찾을 수 없습니다.")
                return
            
            book_uuid = result[0]
            
            # 2. DELETE 수행
            cur.execute("DELETE FROM books WHERE id = %s;", (book_uuid,))
            conn.commit()
            
            if cur.rowcount > 0:
                print(f"✨ '{title}' 도서가 삭제되었습니다.")
            else:
                print(f"'{title}' 도서 삭제에 실패했습니다.")
                
    except psycopg2.Error as e:
        print(f"삭제 오류: {e}")
        conn.rollback()
    finally:
        if conn: conn.close()

# ----------------------------------------------------------------------
# 메인 실행 블록
# ----------------------------------------------------------------------

def main():
    """메인 실행 함수"""
    print("==================================================")
    print("      PostgreSQL CRUD 미션 실행 시작 (psycopg2)     ")
    print("==================================================")
    
    # 1. 테이블 생성
    create_books_table()
    
    # 2. 데이터 삽입
    insert_books()
    
    # 3. SELECT - 삽입 후 전체 데이터 확인
    print("\n--- [초기 데이터] 전체 도서 목록 ---")
    all_books = get_all_books()
    pprint(all_books)
    
    # 4. SELECT - 가격별 조회
    print("\n--- [조회] 25,000원 이상 도서 ---")
    expensive_books = get_expensive_books()
    pprint(expensive_books)
    
    # 5. SELECT - 제목별 조회
    print("\n--- [조회] '파이썬 입문' 도서 ---")
    book_by_title = get_book_by_title("파이썬 입문")
    pprint(book_by_title)

    # 6. UPDATE - '알고리즘 기초' 가격 27,000으로 수정
    print("\n--- [수정] '알고리즘 기초' 가격 변경 ---")
    update_book_price_by_title("알고리즘 기초", 27000)
    
    # 7. UPDATE 결과 확인
    print("\n--- [수정 후] 전체 도서 목록 ---")
    all_books_after_update = get_all_books()
    pprint(all_books_after_update)
    
    # 8. DELETE - '네트워크 이해' 도서 삭제
    print("\n--- [삭제] '네트워크 이해' 도서 ---")
    delete_book_by_title("네트워크 이해")

    # 9. DELETE 결과 확인
    print("\n--- [삭제 후] 최종 도서 목록 ---")
    all_books_after_delete = get_all_books()
    pprint(all_books_after_delete)

    print("\n==================================================")
    print("          PostgreSQL CRUD 미션 실행 완료            ")
    print("==================================================")

if __name__ == '__main__':
    main()