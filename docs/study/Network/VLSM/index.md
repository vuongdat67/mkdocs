# Interactive Learning Dashboard

Hệ thống học tập thông minh với Flashcards, Quiz, Subnet Calculator và theo dõi tiến độ.

<div id="learning-app">
  <style>
    .learning-container {
      max-width: 1200px;
      margin: 0 auto;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin: 30px 0;
    }
    
    .stat-card {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      padding: 25px;
      border-radius: 15px;
      color: white;
      box-shadow: 0 10px 30px rgba(0,0,0,0.1);
      transition: transform 0.3s ease;
    }
    
    .stat-card:hover {
      transform: translateY(-5px);
    }
    
    .stat-number {
      font-size: 42px;
      font-weight: bold;
      margin: 10px 0;
    }
    
    .stat-label {
      font-size: 14px;
      opacity: 0.9;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    
    .tab-container {
      background: white;
      border-radius: 15px;
      box-shadow: 0 5px 25px rgba(0,0,0,0.08);
      overflow: hidden;
      margin: 30px 0;
    }
    
    .tabs {
      display: flex;
      background: #f8f9fa;
      border-bottom: 2px solid #e9ecef;
      overflow-x: auto;
    }
    
    .tab {
      flex: 1;
      min-width: 120px;
      padding: 18px;
      text-align: center;
      cursor: pointer;
      font-weight: 600;
      transition: all 0.3s ease;
      border: none;
      background: transparent;
      color: #6c757d;
      white-space: nowrap;
    }
    
    .tab:hover {
      background: #e9ecef;
    }
    
    .tab.active {
      background: white;
      color: #667eea;
      border-bottom: 3px solid #667eea;
    }
    
    .tab-content {
      padding: 35px;
      min-height: 400px;
    }
    
    .flashcard {
      perspective: 1000px;
      height: 350px;
      margin: 30px auto;
      max-width: 600px;
    }
    
    .flashcard-inner {
      position: relative;
      width: 100%;
      height: 100%;
      text-align: center;
      transition: transform 0.6s;
      transform-style: preserve-3d;
      cursor: pointer;
    }
    
    .flashcard-inner.flipped {
      transform: rotateY(180deg);
    }
    
    .flashcard-front, .flashcard-back {
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      border-radius: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      font-weight: 600;
      padding: 40px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.15);
    }
    
    .flashcard-front {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
    }
    
    .flashcard-back {
      background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
      color: white;
      transform: rotateY(180deg);
    }
    
    .controls {
      display: flex;
      gap: 15px;
      justify-content: center;
      margin-top: 30px;
      flex-wrap: wrap;
    }
    
    .btn {
      padding: 12px 30px;
      border: none;
      border-radius: 25px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.3s ease;
      font-size: 15px;
    }
    
    .btn-primary {
      background: #667eea;
      color: white;
    }
    
    .btn-primary:hover {
      background: #5568d3;
      transform: scale(1.05);
    }
    
    .btn-success {
      background: #00d4aa;
      color: white;
    }
    
    .btn-danger {
      background: #ff6b6b;
      color: white;
    }
    
    .progress-bar-container {
      background: #e9ecef;
      height: 12px;
      border-radius: 10px;
      overflow: hidden;
      margin: 20px 0;
    }
    
    .progress-bar {
      height: 100%;
      background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
      transition: width 0.5s ease;
      border-radius: 10px;
    }
    
    .quiz-option {
      padding: 18px;
      margin: 12px 0;
      border: 2px solid #e9ecef;
      border-radius: 12px;
      cursor: pointer;
      transition: all 0.3s ease;
      background: white;
    }
    
    .quiz-option:hover {
      border-color: #667eea;
      background: #f8f9ff;
      transform: translateX(5px);
    }
    
    .quiz-option.correct {
      background: #d4edda;
      border-color: #28a745;
    }
    
    .quiz-option.wrong {
      background: #f8d7da;
      border-color: #dc3545;
    }
    
    .note-editor {
      width: 100%;
      min-height: 300px;
      padding: 20px;
      border: 2px solid #e9ecef;
      border-radius: 12px;
      font-size: 16px;
      font-family: 'Courier New', monospace;
      resize: vertical;
    }
    
    .note-editor:focus {
      outline: none;
      border-color: #667eea;
    }
    
    .card-counter {
      text-align: center;
      margin: 20px 0;
      font-size: 18px;
      color: #6c757d;
      font-weight: 600;
    }
    
    .hidden {
      display: none;
    }

    /* Subnet Calculator Styles */
    .calc-input-group {
      margin: 20px 0;
    }

    .calc-input-group label {
      display: block;
      margin-bottom: 8px;
      font-weight: 600;
      color: #495057;
    }

    .calc-input {
      width: 100%;
      padding: 12px 15px;
      border: 2px solid #e9ecef;
      border-radius: 8px;
      font-size: 16px;
      transition: border-color 0.3s;
    }

    .calc-input:focus {
      outline: none;
      border-color: #667eea;
    }

    .calc-result {
      background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
      padding: 25px;
      border-radius: 12px;
      margin: 20px 0;
      border-left: 4px solid #667eea;
    }

    .calc-result h4 {
      color: #667eea;
      margin-top: 0;
      margin-bottom: 15px;
    }

    .result-row {
      display: flex;
      justify-content: space-between;
      padding: 10px 0;
      border-bottom: 1px solid #dee2e6;
    }

    .result-row:last-child {
      border-bottom: none;
    }

    .result-label {
      font-weight: 600;
      color: #495057;
    }

    .result-value {
      color: #212529;
      font-family: 'Courier New', monospace;
    }

    .vlsm-input {
      display: flex;
      gap: 10px;
      margin: 10px 0;
      align-items: center;
    }

    .vlsm-input input {
      flex: 1;
    }

    .vlsm-input button {
      padding: 8px 15px;
      background: #dc3545;
      color: white;
      border: none;
      border-radius: 6px;
      cursor: pointer;
    }

    .vlsm-result-table {
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
    }

    .vlsm-result-table th,
    .vlsm-result-table td {
      padding: 12px;
      text-align: left;
      border-bottom: 1px solid #dee2e6;
    }

    .vlsm-result-table th {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      font-weight: 600;
    }

    .vlsm-result-table tr:hover {
      background: #f8f9ff;
    }

    @media (max-width: 768px) {
      .tabs {
        flex-wrap: nowrap;
      }
      .tab {
        font-size: 14px;
        padding: 12px 10px;
      }
      .calc-input-group {
        margin: 15px 0;
      }
      .vlsm-input {
        flex-direction: column;
        align-items: stretch;
      }
    }
  </style>

  <div class="learning-container">
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-label">Tổng thẻ học</div>
        <div class="stat-number" id="total-cards">0</div>
      </div>
      <div class="stat-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
        <div class="stat-label">Đã thuộc</div>
        <div class="stat-number" id="mastered-cards">0</div>
      </div>
      <div class="stat-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
        <div class="stat-label">Đang học</div>
        <div class="stat-number" id="learning-cards">0</div>
      </div>
      <div class="stat-card" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);">
        <div class="stat-label">Tiến độ</div>
        <div class="stat-number" id="progress-percent">0%</div>
      </div>
    </div>

    <div class="tab-container">
      <div class="tabs">
        <button class="tab active" onclick="switchTab('flashcard')">📚 Flashcards</button>
        <button class="tab" onclick="switchTab('quiz')">✍️ Quiz</button>
        <button class="tab" onclick="switchTab('subnet')">🌐 Subnet Calc</button>
        <button class="tab" onclick="switchTab('vlsm')">📊 VLSM</button>
        <button class="tab" onclick="switchTab('notes')">📝 Ghi chú</button>
        <button class="tab" onclick="switchTab('manage')">⚙️ Quản lý</button>
      </div>

      <!-- Flashcard Tab -->
      <div id="flashcard-tab" class="tab-content">
        <div class="card-counter" id="card-counter"></div>
        <div class="flashcard">
          <div class="flashcard-inner" id="flashcard" onclick="flipCard()">
            <div class="flashcard-front">
              <div id="card-question">Click để bắt đầu học!</div>
            </div>
            <div class="flashcard-back">
              <div id="card-answer">Câu trả lời sẽ hiện ở đây</div>
            </div>
          </div>
        </div>
        <div class="progress-bar-container">
          <div class="progress-bar" id="session-progress" style="width: 0%"></div>
        </div>
        <div class="controls">
          <button class="btn btn-danger" onclick="markCard('hard')">😰 Khó</button>
          <button class="btn btn-primary" onclick="markCard('medium')">🤔 Vừa</button>
          <button class="btn btn-success" onclick="markCard('easy')">😊 Dễ</button>
        </div>
      </div>

      <!-- Quiz Tab -->
      <div id="quiz-tab" class="tab-content hidden">
        <h3 id="quiz-question" style="margin-bottom: 30px; font-size: 24px;"></h3>
        <div id="quiz-options"></div>
        <div class="controls">
          <button class="btn btn-primary" onclick="nextQuiz()">Câu tiếp theo →</button>
        </div>
        <div style="margin-top: 30px; text-align: center; font-size: 18px; font-weight: 600;">
          Điểm: <span id="quiz-score">0</span> / <span id="quiz-total">0</span>
        </div>
      </div>

      <!-- Subnet Calculator Tab -->
      <div id="subnet-tab" class="tab-content hidden">
        <h3>🌐 Subnet Calculator</h3>
        
        <div class="calc-input-group">
          <label>Địa chỉ IP:</label>
          <input type="text" class="calc-input" id="ip-input" placeholder="192.168.1.0" value="192.168.1.0">
        </div>

        <div class="calc-input-group">
          <label>CIDR / Subnet Mask:</label>
          <input type="text" class="calc-input" id="cidr-input" placeholder="/24 hoặc 255.255.255.0" value="/24">
        </div>

        <div class="controls">
          <button class="btn btn-primary" onclick="calculateSubnet()">🔢 Tính toán</button>
          <button class="btn btn-success" onclick="clearSubnetCalc()">🔄 Reset</button>
        </div>

        <div id="subnet-result"></div>
      </div>

      <!-- VLSM Tab -->
      <div id="vlsm-tab" class="tab-content hidden">
        <h3>📊 VLSM Calculator</h3>
        
        <div class="calc-input-group">
          <label>Network gốc:</label>
          <input type="text" class="calc-input" id="vlsm-network" placeholder="192.168.1.0/24" value="192.168.1.0/24">
        </div>

        <div class="calc-input-group">
          <label>Yêu cầu subnets (tên:số_hosts):</label>
          <div id="vlsm-requirements">
            <div class="vlsm-input">
              <input type="text" placeholder="LAN A" value="LAN A">
              <input type="number" placeholder="100" value="100" min="1">
              <button onclick="removeVLSMInput(this)">✖</button>
            </div>
          </div>
          <button class="btn btn-success" onclick="addVLSMInput()" style="margin-top: 10px;">➕ Thêm subnet</button>
        </div>

        <div class="controls">
          <button class="btn btn-primary" onclick="calculateVLSM()">🔢 Tính VLSM</button>
          <button class="btn btn-success" onclick="clearVLSM()">🔄 Reset</button>
        </div>

        <div id="vlsm-result"></div>
      </div>

      <!-- Notes Tab -->
      <div id="notes-tab" class="tab-content hidden">
        <h3>📝 Ghi chú của bạn</h3>
        <textarea class="note-editor" id="notes-area" placeholder="Viết ghi chú tại đây...&#10;&#10;Hỗ trợ Markdown:&#10;# Heading&#10;**bold** *italic*&#10;- list item&#10;&#10;Ghi chú tự động lưu!"></textarea>
        <div class="controls">
          <button class="btn btn-primary" onclick="saveNotes()">💾 Lưu ghi chú</button>
          <button class="btn btn-success" onclick="exportNotes()">📤 Xuất file</button>
        </div>
      </div>

      <!-- Manage Tab -->
      <div id="manage-tab" class="tab-content hidden">
        <h3>⚙️ Quản lý thẻ học</h3>
        <div style="margin: 20px 0;">
          <input type="text" id="new-question" placeholder="Câu hỏi / Thuật ngữ" 
            style="width: 100%; padding: 15px; margin: 10px 0; border: 2px solid #e9ecef; border-radius: 8px; font-size: 16px;">
          <textarea id="new-answer" placeholder="Câu trả lời / Định nghĩa" 
            style="width: 100%; padding: 15px; margin: 10px 0; border: 2px solid #e9ecef; border-radius: 8px; min-height: 120px; font-size: 16px;"></textarea>
          <button class="btn btn-success" onclick="addCard()">➕ Thêm thẻ mới</button>
        </div>
        <div id="card-list" style="margin-top: 30px;"></div>
      </div>
    </div>
  </div>

  <script>
    // ============================================
    // LEARNING SYSTEM - Flashcards & Quiz
    // ============================================
    let flashcards = [];
    let currentCardIndex = 0;
    let isFlipped = false;
    let sessionCards = [];
    let quizData = [];
    let currentQuizIndex = 0;
    let quizScore = 0;

    const sampleCards = [
      {
        question: "CIA Triad là gì?",
        answer: "Confidentiality (Bảo mật), Integrity (Toàn vẹn), Availability (Khả dụng) - 3 nguyên tắc cơ bản của an toàn thông tin",
        difficulty: 0,
        lastReview: null
      },
      {
        question: "VLSM là gì?",
        answer: "Variable Length Subnet Mask - Kỹ thuật chia subnet với độ dài mask khác nhau để tối ưu sử dụng địa chỉ IP",
        difficulty: 0,
        lastReview: null
      },
      {
        question: "Subnet Mask /24 có bao nhiêu hosts?",
        answer: "254 hosts (2^8 - 2 = 256 - 2)",
        difficulty: 0,
        lastReview: null
      }
    ];

    function init() {
      const saved = localStorage.getItem('learningCards');
      flashcards = saved ? JSON.parse(saved) : sampleCards;
      
      const savedNotes = localStorage.getItem('learningNotes');
      if (savedNotes) {
        document.getElementById('notes-area').value = savedNotes;
      }
      
      sessionCards = [...flashcards];
      updateStats();
      displayCard();
      renderCardList();
    }

    function saveData() {
      localStorage.setItem('learningCards', JSON.stringify(flashcards));
    }

    function updateStats() {
      const total = flashcards.length;
      const mastered = flashcards.filter(c => c.difficulty >= 3).length;
      const learning = total - mastered;
      const progress = total > 0 ? Math.round((mastered / total) * 100) : 0;

      document.getElementById('total-cards').textContent = total;
      document.getElementById('mastered-cards').textContent = mastered;
      document.getElementById('learning-cards').textContent = learning;
      document.getElementById('progress-percent').textContent = progress + '%';
    }

    function displayCard() {
      if (sessionCards.length === 0) {
        document.getElementById('card-question').textContent = '🎉 Hoàn thành! Bạn đã học hết thẻ!';
        document.getElementById('card-answer').textContent = 'Tuyệt vời!';
        return;
      }

      const card = sessionCards[currentCardIndex];
      document.getElementById('card-question').textContent = card.question;
      document.getElementById('card-answer').textContent = card.answer;
      
      const remaining = sessionCards.length - currentCardIndex;
      document.getElementById('card-counter').textContent = 
        `Thẻ ${currentCardIndex + 1} / ${sessionCards.length} (còn ${remaining} thẻ)`;
      
      const progress = ((currentCardIndex + 1) / sessionCards.length) * 100;
      document.getElementById('session-progress').style.width = progress + '%';
    }

    function flipCard() {
      const card = document.getElementById('flashcard');
      isFlipped = !isFlipped;
      if (isFlipped) {
        card.classList.add('flipped');
      } else {
        card.classList.remove('flipped');
      }
    }

    function markCard(level) {
      if (sessionCards.length === 0) return;

      const card = sessionCards[currentCardIndex];
      const cardInDb = flashcards.find(c => c.question === card.question);
      
      if (level === 'easy') {
        cardInDb.difficulty = Math.min(cardInDb.difficulty + 1, 5);
      } else if (level === 'hard') {
        cardInDb.difficulty = Math.max(cardInDb.difficulty - 1, 0);
      }
      
      cardInDb.lastReview = new Date().toISOString();
      
      currentCardIndex++;
      if (currentCardIndex >= sessionCards.length) {
        currentCardIndex = 0;
        sessionCards = flashcards.filter(c => c.difficulty < 3);
        if (sessionCards.length === 0) {
          sessionCards = [...flashcards];
        }
      }

      if (isFlipped) flipCard();
      displayCard();
      updateStats();
      saveData();
    }

    function switchTab(tabName) {
      document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.add('hidden'));
      
      event.target.classList.add('active');
      document.getElementById(tabName + '-tab').classList.remove('hidden');
      
      if (tabName === 'quiz') {
        startQuiz();
      }
    }

    function startQuiz() {
      quizData = [...flashcards].sort(() => Math.random() - 0.5).slice(0, 5);
      currentQuizIndex = 0;
      quizScore = 0;
      displayQuiz();
    }

    function displayQuiz() {
      if (currentQuizIndex >= quizData.length) {
        document.getElementById('quiz-question').textContent = 
          `🎊 Hoàn thành! Điểm của bạn: ${quizScore}/${quizData.length}`;
        document.getElementById('quiz-options').innerHTML = '';
        return;
      }

      const card = quizData[currentQuizIndex];
      document.getElementById('quiz-question').textContent = card.question;
      document.getElementById('quiz-score').textContent = quizScore;
      document.getElementById('quiz-total').textContent = quizData.length;

      const options = [card.answer];
      const wrongAnswers = flashcards
        .filter(c => c.answer !== card.answer)
        .sort(() => Math.random() - 0.5)
        .slice(0, 3)
        .map(c => c.answer);
      
      options.push(...wrongAnswers);
      options.sort(() => Math.random() - 0.5);

      const optionsHtml = options.map((opt, i) => 
        `<div class="quiz-option" onclick="checkAnswer(this, '${card.answer.replace(/'/g, "\\'")}')">${opt}</div>`
      ).join('');
      
      document.getElementById('quiz-options').innerHTML = optionsHtml;
    }

    function checkAnswer(element, correctAnswer) {
      const isCorrect = element.textContent === correctAnswer;
      element.classList.add(isCorrect ? 'correct' : 'wrong');
      
      if (isCorrect) {
        quizScore++;
        document.getElementById('quiz-score').textContent = quizScore;
      }

      document.querySelectorAll('.quiz-option').forEach(opt => {
        opt.style.pointerEvents = 'none';
        if (opt.textContent === correctAnswer) {
          opt.classList.add('correct');
        }
      });
    }

    function nextQuiz() {
      currentQuizIndex++;
      displayQuiz();
    }

    function addCard() {
      const question = document.getElementById('new-question').value.trim();
      const answer = document.getElementById('new-answer').value.trim();
      
      if (!question || !answer) {
        alert('Vui lòng điền đầy đủ câu hỏi và câu trả lời!');
        return;
      }

      flashcards.push({
        question: question,
        answer: answer,
        difficulty: 0,
        lastReview: null
      });

      document.getElementById('new-question').value = '';
      document.getElementById('new-answer').value = '';
      
      saveData();
      updateStats();
      renderCardList();
      alert('✅ Đã thêm thẻ mới!');
    }

    function renderCardList() {
      const html = flashcards.map((card, index) => `
        <div style="padding: 15px; margin: 10px 0; border: 2px solid #e9ecef; border-radius: 10px; background: white;">
          <strong>Q:</strong> ${card.question}<br>
          <strong>A:</strong> ${card.answer}<br>
          <small style="color: #6c757d;">Độ khó: ${'⭐'.repeat(card.difficulty)}</small>
          <button onclick="deleteCard(${index})" style="float: right; background: #ff6b6b; color: white; border: none; padding: 8px 15px; border-radius: 5px; cursor: pointer;">🗑️ Xóa</button>
        </div>
      `).join('');
      
      document.getElementById('card-list').innerHTML = html;
    }

    function deleteCard(index) {
      if (confirm('Bạn có chắc muốn xóa thẻ này?')) {
        flashcards.splice(index, 1);
        saveData();
        updateStats();
        renderCardList();
      }
    }

    function saveNotes() {
      const notes = document.getElementById('notes-area').value;
      localStorage.setItem('learningNotes', notes);
      alert('✅ Đã lưu ghi chú!');
    }

    function exportNotes() {
      const notes = document.getElementById('notes-area').value;
      const blob = new Blob([notes], { type: 'text/markdown' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'learning-notes.md';
      a.click();
    }

    document.getElementById('notes-area')?.addEventListener('input', () => {
      const notes = document.getElementById('notes-area').value;
      localStorage.setItem('learningNotes', notes);
    });

    // ============================================
    // SUBNET CALCULATOR
    // ============================================
    
    function ipToInt(ip) {
      return ip.split('.').reduce((acc, octet) => (acc << 8) + parseInt(octet), 0) >>> 0;
    }

    function intToIp(int) {
      return [
        (int >>> 24) & 255,
        (int >>> 16) & 255,
        (int >>> 8) & 255,
        int & 255
      ].join('.');
    }

    function cidrToMask(cidr) {
      const mask = ~((1 << (32 - cidr)) - 1);
      return intToIp(mask >>> 0);
    }

    function maskToCidr(mask) {
      return mask.split('.').map(octet => 
        parseInt(octet).toString(2).split('1').length - 1
      ).reduce((a, b) => a + b);
    }

    function calculateSubnet() {
      const ipInput = document.getElementById('ip-input').value.trim();
      const cidrInput = document.getElementById('cidr-input').value.trim();

      // Parse IP
      const ipMatch = ipInput.match(/^(\d{1,3}\.){3}\d{1,3}$/);
      if (!ipMatch) {
        alert('❌ IP không hợp lệ! Ví dụ: 192.168.1.0');
        return;
      }

      // Parse CIDR
      let cidr;
      if (cidrInput.startsWith('/')) {
        cidr = parseInt(cidrInput.substring(1));
      } else if (cidrInput.includes('.')) {
        cidr = maskToCidr(cidrInput);
      } else {
        cidr = parseInt(cidrInput);
      }

      if (cidr < 0 || cidr > 32) {
        alert('❌ CIDR không hợp lệ! Phải từ 0-32');
        return;
      }

      // Calculate
      const ipInt = ipToInt(ipInput);
      const maskInt = ~((1 << (32 - cidr)) - 1) >>> 0;
      const wildcardInt = ~maskInt >>> 0;
      
      const networkInt = (ipInt & maskInt) >>> 0;
      const broadcastInt = (networkInt | wildcardInt) >>> 0;
      const firstHostInt = networkInt + 1;
      const lastHostInt = broadcastInt - 1;
      
      const totalHosts = Math.pow(2, 32 - cidr);
      const usableHosts = cidr === 31 ? 2 : (cidr === 32 ? 1 : totalHosts - 2);
      
      const subnetMask = intToIp(maskInt);
      const wildcardMask = intToIp(wildcardInt);
      const networkAddr = intToIp(networkInt);
      const broadcastAddr = intToIp(broadcastInt);
      const firstHost = intToIp(firstHostInt);
      const lastHost = intToIp(lastHostInt);
      
      // Determine class
      const firstOctet = parseInt(ipInput.split('.')[0]);
      let ipClass = '';
      if (firstOctet >= 1 && firstOctet <= 126) ipClass = 'A';
      else if (firstOctet >= 128 && firstOctet <= 191) ipClass = 'B';
      else if (firstOctet >= 192 && firstOctet <= 223) ipClass = 'C';
      else if (firstOctet >= 224 && firstOctet <= 239) ipClass = 'D (Multicast)';
      else ipClass = 'E (Reserved)';
      
      // Binary representation
      const ipBinary = ipInput.split('.').map(o => 
        parseInt(o).toString(2).padStart(8, '0')
      ).join('.');
      
      const maskBinary = subnetMask.split('.').map(o => 
        parseInt(o).toString(2).padStart(8, '0')
      ).join('.');

      // Display results
      document.getElementById('subnet-result').innerHTML = `
        <div class="calc-result">
          <h4>📊 Kết quả tính toán</h4>
          
          <div class="result-row">
            <span class="result-label">IP Address:</span>
            <span class="result-value">${ipInput}</span>
          </div>
          
          <div class="result-row">
            <span class="result-label">Subnet Mask:</span>
            <span class="result-value">${subnetMask} (/${cidr})</span>
          </div>
          
          <div class="result-row">
            <span class="result-label">Wildcard Mask:</span>
            <span class="result-value">${wildcardMask}</span>
          </div>
          
          <div class="result-row">
            <span class="result-label">Network Address:</span>
            <span class="result-value">${networkAddr}/${cidr}</span>
          </div>
          
          <div class="result-row">
            <span class="result-label">Broadcast Address:</span>
            <span class="result-value">${broadcastAddr}</span>
          </div>
          
          <div class="result-row">
            <span class="result-label">First Host:</span>
            <span class="result-value">${firstHost}</span>
          </div>
          
          <div class="result-row">
            <span class="result-label">Last Host:</span>
            <span class="result-value">${lastHost}</span>
          </div>
          
          <div class="result-row">
            <span class="result-label">Usable Hosts:</span>
            <span class="result-value">${usableHosts.toLocaleString()}</span>
          </div>
          
          <div class="result-row">
            <span class="result-label">Total Addresses:</span>
            <span class="result-value">${totalHosts.toLocaleString()}</span>
          </div>
          
          <div class="result-row">
            <span class="result-label">IP Class:</span>
            <span class="result-value">${ipClass}</span>
          </div>
        </div>
        
        <div class="calc-result">
          <h4>🔢 Binary Representation</h4>
          
          <div class="result-row">
            <span class="result-label">IP Binary:</span>
            <span class="result-value">${ipBinary}</span>
          </div>
          
          <div class="result-row">
            <span class="result-label">Mask Binary:</span>
            <span class="result-value">${maskBinary}</span>
          </div>
          
          <div class="result-row">
            <span class="result-label">Network Bits:</span>
            <span class="result-value">${cidr} bits</span>
          </div>
          
          <div class="result-row">
            <span class="result-label">Host Bits:</span>
            <span class="result-value">${32 - cidr} bits</span>
          </div>
        </div>
        
        <div class="calc-result">
          <h4>📝 CIDR Notation</h4>
          <div class="result-row">
            <span class="result-label">CIDR Block:</span>
            <span class="result-value">${networkAddr}/${cidr}</span>
          </div>
          <div class="result-row">
            <span class="result-label">IP Range:</span>
            <span class="result-value">${firstHost} - ${lastHost}</span>
          </div>
        </div>
      `;
    }

    function clearSubnetCalc() {
      document.getElementById('ip-input').value = '192.168.1.0';
      document.getElementById('cidr-input').value = '/24';
      document.getElementById('subnet-result').innerHTML = '';
    }

    // ============================================
    // VLSM CALCULATOR
    // ============================================
    
    function addVLSMInput() {
      const container = document.getElementById('vlsm-requirements');
      const div = document.createElement('div');
      div.className = 'vlsm-input';
      div.innerHTML = `
        <input type="text" placeholder="Tên subnet">
        <input type="number" placeholder="Số hosts" min="1">
        <button onclick="removeVLSMInput(this)">✖</button>
      `;
      container.appendChild(div);
    }

    function removeVLSMInput(btn) {
      btn.parentElement.remove();
    }

    function calculateVLSM() {
      const networkInput = document.getElementById('vlsm-network').value.trim();
      
      // Parse network
      const match = networkInput.match(/^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\/(\d{1,2})$/);
      if (!match) {
        alert('❌ Network không hợp lệ! Ví dụ: 192.168.1.0/24');
        return;
      }
      
      const baseIp = match[1];
      const baseCidr = parseInt(match[2]);
      
      // Get requirements
      const inputs = document.querySelectorAll('#vlsm-requirements .vlsm-input');
      const requirements = [];
      
      inputs.forEach(input => {
        const name = input.querySelector('input[type="text"]').value.trim();
        const hosts = parseInt(input.querySelector('input[type="number"]').value);
        
        if (name && hosts > 0) {
          requirements.push({ name, hosts });
        }
      });
      
      if (requirements.length === 0) {
        alert('❌ Vui lòng thêm ít nhất 1 subnet requirement!');
        return;
      }
      
      // Sort by hosts descending
      requirements.sort((a, b) => b.hosts - a.hosts);
      
      // Calculate subnets
      const subnets = [];
      let currentIpInt = ipToInt(baseIp);
      const baseNetwork = (currentIpInt & (~((1 << (32 - baseCidr)) - 1) >>> 0)) >>> 0;
      const baseSize = Math.pow(2, 32 - baseCidr);
      
      currentIpInt = baseNetwork;
      
      for (const req of requirements) {
        // Calculate required prefix
        let hostBits = 0;
        let capacity = 0;
        
        for (let h = 1; h <= 32; h++) {
          capacity = Math.pow(2, h) - 2;
          if (capacity >= req.hosts) {
            hostBits = h;
            break;
          }
        }
        
        const cidr = 32 - hostBits;
        const maskInt = ~((1 << hostBits) - 1) >>> 0;
        const blockSize = Math.pow(2, hostBits);
        
        // Align to block boundary
        currentIpInt = (Math.floor(currentIpInt / blockSize) * blockSize) >>> 0;
        
        const networkInt = currentIpInt;
        const broadcastInt = (networkInt + blockSize - 1) >>> 0;
        const firstHostInt = networkInt + 1;
        const lastHostInt = broadcastInt - 1;
        
        subnets.push({
          name: req.name,
          requiredHosts: req.hosts,
          cidr: cidr,
          network: intToIp(networkInt),
          firstHost: intToIp(firstHostInt),
          lastHost: intToIp(lastHostInt),
          broadcast: intToIp(broadcastInt),
          usableHosts: capacity,
          mask: cidrToMask(cidr)
        });
        
        currentIpInt = broadcastInt + 1;
        
        // Check if we exceeded base network
        if (currentIpInt > baseNetwork + baseSize) {
          alert('⚠️ Không đủ địa chỉ IP trong network gốc!');
          break;
        }
      }
      
      // Display results
      let html = `
        <div class="calc-result">
          <h4>📊 Kết quả VLSM</h4>
          <p><strong>Network gốc:</strong> ${networkInput}</p>
          <p><strong>Tổng subnets:</strong> ${subnets.length}</p>
        </div>
        
        <table class="vlsm-result-table">
          <thead>
            <tr>
              <th>Subnet Name</th>
              <th>Hosts Cần</th>
              <th>CIDR</th>
              <th>Network</th>
              <th>First Host</th>
              <th>Last Host</th>
              <th>Broadcast</th>
              <th>Usable</th>
            </tr>
          </thead>
          <tbody>
      `;
      
      subnets.forEach(subnet => {
        html += `
          <tr>
            <td><strong>${subnet.name}</strong></td>
            <td>${subnet.requiredHosts}</td>
            <td>/${subnet.cidr}</td>
            <td>${subnet.network}</td>
            <td>${subnet.firstHost}</td>
            <td>${subnet.lastHost}</td>
            <td>${subnet.broadcast}</td>
            <td>${subnet.usableHosts}</td>
          </tr>
        `;
      });
      
      html += `
          </tbody>
        </table>
      `;
      
      // Summary
      const totalUsed = subnets.reduce((acc, s) => acc + Math.pow(2, 32 - s.cidr), 0);
      const totalAvailable = baseSize;
      const remaining = totalAvailable - totalUsed;
      
      html += `
        <div class="calc-result">
          <h4>📈 Tổng kết</h4>
          <div class="result-row">
            <span class="result-label">Tổng địa chỉ available:</span>
            <span class="result-value">${totalAvailable.toLocaleString()}</span>
          </div>
          <div class="result-row">
            <span class="result-label">Đã sử dụng:</span>
            <span class="result-value">${totalUsed.toLocaleString()}</span>
          </div>
          <div class="result-row">
            <span class="result-label">Còn lại:</span>
            <span class="result-value">${remaining.toLocaleString()} (${((remaining/totalAvailable)*100).toFixed(2)}%)</span>
          </div>
        </div>
      `;
      
      document.getElementById('vlsm-result').innerHTML = html;
    }

    function clearVLSM() {
      document.getElementById('vlsm-network').value = '192.168.1.0/24';
      document.getElementById('vlsm-requirements').innerHTML = `
        <div class="vlsm-input">
          <input type="text" placeholder="LAN A" value="LAN A">
          <input type="number" placeholder="100" value="100" min="1">
          <button onclick="removeVLSMInput(this)">✖</button>
        </div>
      `;
      document.getElementById('vlsm-result').innerHTML = '';
    }

    // Initialize on load
    init();
  </script>
</div>

---

## 📖 Hướng dẫn sử dụng

### 1️⃣ Tab Flashcards
- Click vào thẻ để lật và xem câu trả lời
- Đánh giá độ khó: **Dễ** (tăng độ thành thạo), **Vừa** (giữ nguyên), **Khó** (giảm độ thành thạo)
- Hệ thống sẽ ưu tiên các thẻ bạn chưa thuộc

### 2️⃣ Tab Quiz
- Kiểm tra kiến thức với câu hỏi trắc nghiệm
- Hệ thống tự động tạo câu sai từ các thẻ khác
- Xem điểm số ngay lập tức

### 3️⃣ Tab Subnet Calculator
- Nhập địa chỉ IP và CIDR/Subnet Mask
- Tự động tính: Network, Broadcast, First/Last Host, số hosts
- Hiển thị binary representation
- Hỗ trợ tất cả CIDR từ /0 đến /32

**Ví dụ**:
```
IP: 192.168.1.100
CIDR: /26 hoặc 255.255.255.192
```

### 4️⃣ Tab VLSM Calculator
- Nhập network gốc (ví dụ: 192.168.1.0/24)
- Thêm các subnet requirements (tên và số hosts)
- Hệ thống tự động:
  - Sắp xếp theo thứ tự giảm dần
  - Tính CIDR phù hợp
  - Gán địa chỉ không overlap
  - Hiển thị bảng chi tiết

**Ví dụ**:
```
Network: 192.168.1.0/24
Requirements:
- LAN A: 100 hosts → /25
- LAN B: 50 hosts → /26
- LAN C: 20 hosts → /27
```

### 5️⃣ Tab Ghi chú
- Viết ghi chú với Markdown
- Tự động lưu vào trình duyệt
- Xuất ra file `.md`

### 6️⃣ Tab Quản lý
- Thêm thẻ học mới
- Xóa thẻ không cần thiết
- Xem độ khó của từng thẻ

---

## 🎯 Tính năng Subnet Calculator

### Hỗ trợ input
- ✅ CIDR notation: `/24`, `/26`, `/30`
- ✅ Subnet mask: `255.255.255.0`, `255.255.255.192`
- ✅ Số đơn: `24`, `26`, `30`

### Output chi tiết
- 📊 Network Address
- 📡 Broadcast Address
- 🖥️ First/Last Host
- 📈 Usable Hosts count
- 🔢 Binary representation
- 🏷️ IP Class determination
- 🌐 Wildcard mask

### VLSM Features
- 🔄 Tự động sắp xếp requirements
- 📐 Tính toán CIDR tối ưu
- 🎯 Gán địa chỉ không overlap
- 📊 Bảng kết quả chi tiết
- 📈 Thống kê sử dụng IP

---

## 💡 Tips sử dụng

### Subnet Calculator Tips
1. **Quick CIDR**: Nhập `/24` thay vì `255.255.255.0`
2. **Check overlap**: Tính nhiều subnet để kiểm tra overlap
3. **Binary view**: Xem binary để hiểu rõ subnet mask

### VLSM Tips
1. **Từ lớn đến nhỏ**: Luôn nhập subnet lớn nhất trước
2. **Round up**: Hệ thống tự động round lên power of 2
3. **Check remaining**: Xem phần còn lại để mở rộng sau

---

## 🔗 Tài liệu liên quan

- [📚 Subnet Reference Complete](subnet-reference.md) - Bảng đầy đủ + công thức
- [🎓 VLSM Tutorial](vlsm-tutorial.md) - Hướng dẫn chi tiết VLSM
- [📊 Subnetting Practice](subnetting-practice.md) - Bài tập thực hành

---

*Cập nhật: 2024 | Tích hợp Subnet Calculator & VLSM*