// 코드를 작성해 주세요<!DOCTYPE html>





<body>
  <div class="container">
    <h1>가위 바위 보</h1>
    <header class="row">
      <span class="m-1">Player1</span>
      <span class="m-1">vs</span>
      <span class="m-1">Player2</span>
    </header>
    <div class="row">
      <span class="countA m-1">0</span>
      <span class="countB m-1">0</span>
    </div>
    <main class="row">
      <div class="player m-1">
        <img draggable="false" id="player1-img" src="./img/scissors.png" alt="">
      </div>
      <div class="player m-1">
        <img draggable="false" id="player2-img" src="./img/scissors.png" alt="">
      </div>
    </main>
    <section class="row button-box">
      <button id="scissors-button" class="m-1">
        <img draggable="false" src="./img/scissors.png" alt="">
      </button>
      <button id="rock-button" class="m-1">
        <img draggable="false" src="./img/rock.png" alt="">
      </button>
      <button id="paper-button" class="m-1">
        <img draggable="false" src="./img/paper.png" alt="">
      </button>
    </section>
  </div>
  <div class="modal">
    <div class="modal-content"></div>
  </div>
  <script src="./index.js"></script>
</body>
</html>