$(document).ready(function(){       
   var scroll_start = 0;
   var startchange = $('#slider').height()/2;
   $(document).scroll(function() { 
      scroll_start = $(this).scrollTop();
      if(scroll_start > startchange) {
          $('header').css({'background-color': '#029acf', 'border-bottom':'1px solid #c4c4c4'});
       } else {
          $('header').css({'background-color': 'transparent', 'border':'0'});
       }
   });
});