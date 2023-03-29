import styled from "./Home.module.css";

function Home() {
  const login = (adress, e) => {
    window.location.href = adress;
  };

  return (
    <div>
      <div>
        <header className={styled.header}>
          <div>
            <button className={styled.accountButton} onClick={(e) => login("/login", e)}>
              로그인
            </button>
          </div>
        </header>
      </div>
      <div className={styled.container}>
        <section>
          <p>Hello world!</p>
        </section>
      </div>
    </div>
  );
}

export default Home;
