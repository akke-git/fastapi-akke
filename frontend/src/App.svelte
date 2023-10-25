<script>

import Router from 'svelte-spa-router'
import Home from './routes/home.svelte'
import Detail from "./routes/detail.svelte"
import QuestionCreate from "./routes/QuestionCreate.svelte"
import Navigation from "./components/navigation.svelte"
import UserCreate from "./routes/UserCreate.svelte"
import UserLogin from "./routes/UserLogin.svelte"
import QuestionModify from "./routes/QuestionModify.svelte"
import AnswerModify from "./routes/AnswerModify.svelte"


const routes = {
  '/':Home,
  '/detail/:question_id': Detail,
  '/question-create': QuestionCreate,
  '/user-create': UserCreate,
  '/user-login': UserLogin,
  '/question-modify/:question_id': QuestionModify,
  '/answer-modify/:answer_id': AnswerModify,
}
//    / 주소에 매핑되는 컴포넌트로 <Home />을 등록했다. 여기서 <Home />은 새로 작성한 Home.svelte 파일의 내용을 의미한다. 
// 이 후 추가되는 URL 규칙들도 routes 변수에 추가하면 된다.

</script>

<Navigation />

<Router {routes}/>





<!-- 1차 실습 --------------------------------------------------------------------------------------------->
<!-- 
  let message;

  fetch("http://127.0.0.1:8000/hello").then((response) => {
    response.json().then((json) => {
      message = json.message;
    });
  });
</script>

<h1>{message}</h1>

-->





<!-- 원본 ----------------------------------------------------------------------------------------------->

<!-- <script>
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
</script>

<main>
  <div>
    <a href="https://vitejs.dev" target="_blank" rel="noreferrer">
      <img src={viteLogo} class="logo" alt="Vite Logo" />
    </a>
    <a href="https://svelte.dev" target="_blank" rel="noreferrer">
      <img src={svelteLogo} class="logo svelte" alt="Svelte Logo" />
    </a>
  </div>
  <h1>Vite + Svelte</h1>

  <div class="card">
    <Counter />
  </div>

  <p>
    Check out <a href="https://github.com/sveltejs/kit#readme" target="_blank" rel="noreferrer">SvelteKit</a>, the official Svelte app framework powered by Vite!
  </p>

  <p class="read-the-docs">
    Click on the Vite and Svelte logos to learn more
  </p>
</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
</style> -->
