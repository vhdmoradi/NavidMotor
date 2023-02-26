// $(".sidebar a").on("click", function (){
//     $(".fa-rotate-270").removeClass("fa-rotate-270");
//     // jQuery(this).find("i").removeClass(("fa-rotate-270"));
//     if (!jQuery(this).find("i").hasClass("fa-rotate-270")) {
//         jQuery(this).find("i").addClass(("fa-rotate-270"));
//     }else {
//         jQuery(this).find("i").removeClass(("fa-rotate-270"));
//     }
// })
 let menu_btn = document.querySelector("#menu_btn");
    let sidebar = document.getElementsByClassName("bg-overlay")[0];
    function showSidebar() {
      sidebar.classList.add('show');
    }
    function hideSidebar() {
      sidebar.classList.remove('show');
    }
document.querySelectorAll(".sidebar li").forEach(function (e){
        e.addEventListener("click", changeIconDirection)
})
function changeIconDirection(e) {

}

$(".open-btn").on("click", function (){
        $(".sidebar").addClass("active");
        $(".open-btn").addClass("visually-hidden");
})
$(".close-btn").on("click", function (){
        $(".sidebar").removeClass("active");
        setTimeout(function (){
            $(".open-btn").removeClass("visually-hidden");
        }, 250);
})
// $(".header_selector").on("click", function(){
//     $(".active-header").removeClass("active-header");
//     $(this).addClass("active-header");
// })
