// *****FOR IMAGE SLIDER******

    let slideIndex = 0;
    let maxSlideIndex = 0;
    let second = 0;
    function showSlides() {
        let i;
        let slides = document.getElementsByClassName("slider-image");
        let pointer = document.getElementsByClassName("dot");
        if (slideIndex > slides.length-1) {slideIndex = 0}
        if(maxSlideIndex>0){
            maxSlideIndex=0;
        }    
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";  
            maxSlideIndex++;
            pointer[i].children[0].classList.remove('active');
        }
        slides[slideIndex].style.display = "block";
        pointer[slideIndex].children[0].classList.add('active');
        slideIndex++;
        second=0;      
    }
    showSlides();
        setInterval(() => {
            if(second>=2){
                showSlides();
            }
        }, 3000);
    function left(){
        if((slideIndex-1)==0){
            slideIndex = maxSlideIndex-1;
        }
        else{
            slideIndex = slideIndex-2;
        }
        showSlides();
    }
    function right(){
        showSlides();
    }
    setInterval(() => {
        second++;
        if(second==3){
            second==0;
        }
    }, 1000);

    function move(index){
        slideIndex = index;
        showSlides();
    }

    // *****FOR CARD SLIDER******
    
    window.addEventListener("resize", reset);
    function reset(){
        activeCards = 1;
        smActiveCards = 1;
    }
    let TotalCards = 0;
    let activeCards = 1;
    let smActiveCards = 1;
    function rightCard(){
        let i=0;
        let card = document.getElementsByClassName("s-card");
        if(window.innerWidth<=576){
            
            if(smActiveCards!==(card.length)){
                for (i = 0; i < card.length; i++) {
                    if(smActiveCards==1){
                        card[i].style.right ="0%";
                    }
                    if(window.innerWidth<=400){
                        card[i].style.right = (10.4*smActiveCards)+"%";
                    }
                    else{
                        card[i].style.right = (10.1*smActiveCards)+"%";
                    }
                    card[i].style.left = "auto";
                }
                smActiveCards++;

            }
            console.log(smActiveCards,card.length);
            
        }
        else{
            if(activeCards!==(TotalCards-2)){
                TotalCards =0;
                for (i = 0; i < card.length; i++) {
                    if(activeCards==1){
                        card[i].style.right ="0%";
                    }
                    if(window.innerWidth<=905 && window.innerWidth>709){
                        card[i].style.right = (3.4*activeCards)+"%";
                    }
                    else if(window.innerWidth<=709 && window.innerWidth>576){
                        card[i].style.right = (4.9*activeCards)+"%";
                    }
                    else{
                        card[i].style.right = (3.3*activeCards)+"%";
                    } 
                    card[i].style.left = "auto";
                    TotalCards++;
                }
                activeCards++;
            }
        }   
    }
    function leftCard(){
        let i=0;
        let card = document.getElementsByClassName("s-card");
        if(activeCards!==1 || smActiveCards!==1){
            TotalCards =0;
            console.log(smActiveCards,activeCards);
            for (i = 0; i < card.length; i++) {
                let recent = card[i].style.right;
                //recent = Number(recent);
                recent =  recent.match(/\d+(\W\d+)?/ig);
                recent = recent[0];
                if(window.innerWidth<=905 && window.innerWidth>709){
                    card[i].style.right = (recent-3.4)+"%";
                }
                else if(window.innerWidth<=709 && window.innerWidth>576){
                    card[i].style.right = (recent-4.9)+"%";
                }
                else if(window.innerWidth<=576 && window.innerWidth>400){
                    card[i].style.right = (recent-10.1)+"%";
                }
                else if(window.innerWidth <= 470){
                    card[i].style.right = (recent-10.4)+"%";
                }
                else{
                    card[i].style.right = (recent-3.3)+"%";
                }
                card[i].style.left = "auto";
                TotalCards++;
            }
           
            if(window.innerWidth<=576){
                smActiveCards--;
            }
            else{
                activeCards--;
            }
        }
        else{
           for (i = 0; i < card.length; i++) {
            card[i].style.right ="0%";
           } 
        }
    }
    