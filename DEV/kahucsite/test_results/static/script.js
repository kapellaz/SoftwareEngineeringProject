const quizClass = document.getElementsByClassName('contentBox');

for (i = 0; i < quizClass.length; i++){
    quizClass[i].addEventListener('click', function(){
        this.classList.toggle('active')
    })
}



