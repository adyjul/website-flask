(function ($) {
  "use strict";

  // if ($(".carousel-item .active")) {
  //   console.log("hai");
  // } else if ($(".carousel-item")) {
  //   console.log("kk");
  // }

  // $('.scroll-to-section').on('click',function(e){
  // 	var tujuan = $this.attr('href');
  // 	var elementTujuan = $(tujuan);
  // 	$('body').animate({
  // 		scrollTop : elementTujuan.offset().top-50
  // 	},1000,'easeInOutExpo')
  // })

  var elementWindow = $(document).width();
  if (979 >= elementWindow) {
    $(".modal-dialog").css("height","70%");    
  } 
  $(window).resize(function () {
    // console.log($(document).width())
    var element = $(document).width();
    if (979 >= element) {
      $(".modal-dialog").css("height","70%");  
    } 
  });

  var scrollLink = $(".scroll-to-section");
  scrollLink.click(function (e) {
    e.preventDefault();
    $("body,html").animate(
      {
        scrollTop: $(this.hash).offset().top - 70,
      },
      1000,
      "easeInOutExpo"
    );
  });

  $(window).scroll(function () {
    var scroll = $(window).scrollTop();
    var box = $(".hero-slides").height() - 20;
    var header = $(".navbar").height();

    if (scroll >= box - header) {
      $(".navbar").addClass("fixed-top");      
    } else {
      $(".navbar").removeClass("fixed-top");
    }
  });

  $(".berita").owlCarousel({
    autoplay: true,
    dots: false,
    loop: true,
    nav: true,
    margin: 80,
    responsive: {
      0: {
        items: 1,
      },
      576: {
        items: 1,
      },
      768: {
        items: 2,
      },
      992: {
        items: 3,
      },
    },
  });

  $(".card-content").owlCarousel({
    autoplay: true,
    dots: false,
    loop: true,
    nav: true, 
    margin : 80,   
    responsive: {
      0: {
        items: 1,
      },
      576: {
        items: 1,
      },
      768: {
        items: 2,
      },
      992: {
        items: 3,
      },
    },
  });

  // Window Resize Mobile Menu Fix
  

  // Scroll animation init
  

  // Window Resize Mobile Menu Fix
 

  // Window Resize Mobile Menu Fix
  
})(window.jQuery);
