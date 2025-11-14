let scrollContainer = document.querySelector(".gallery");
            let backBtn = document.getElementById("backBtn");
            let nextBtn = document.getElementById("nextBtn");

            scrollContainer.addEventListener("wheel", (evt) => {
                evt.preventDefault();
                scrollContainer.scrollLeft += evt.deltaY;
                scrollContainer.style.scrollBehavior = "auto";
            });

            nextBtn.addEventListener("click", () =>{
                scrollContainer.style.scrollBehavior = "smooth";
                scrollContainer.scrollLeft +=2000;
            });
            backBtn.addEventListener("click", () =>{
                scrollContainer.style.scrollBehavior = "smooth";
                scrollContainer.scrollLeft -=2000;
            });
            function unfold(){
                document.getElementById("abt-txt").innerHTML = "I am an I.T. student with a dream to be a Software Engineer.\nThis portfolio contains with the basic information about me.\nI Studied at General De Jesus College for the 1st year of my College Life\nand transferred in Nueva Ecija University of Science And Techonology\nto seek for better opportunities.\nThis coming school year I'm going to be a regular sophomore \nand I want to focus more on Web Development and Software Development..";
            }
            function fold(){
                document.getElementById("abt-txt").innerHTML = " ";
            }