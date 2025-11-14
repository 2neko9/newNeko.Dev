function toggleMenu(){
    const sidebar = document.getElementById("menuSidebar");
    const content = document.querySelector(".content");

    sidebar.classList.toggle("open");
    content.classList.toggle("open");
  }