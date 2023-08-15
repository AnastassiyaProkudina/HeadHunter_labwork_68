const searchBtn = document.querySelector(".search-btn");
const vacancySearch = document.querySelector("#vacancy_search");

searchBtn.addEventListener("click", function () {
    if (vacancySearch.style.display === "none") {
        vacancySearch.style.display = "flex";
    } else {
        vacancySearch.style.display = "none";
    }
});
jQuery(document).ready(function ($) {
    $('.vacancy-search').on('keyup', function () {
        const searchVacancy = $(this).val().toLowerCase();
        $('.vacancy').each(function (idx, item) {
            let vacancy = $(item).attr("data-vacancy").toLowerCase();
            if (vacancy.includes(searchVacancy) || searchVacancy.length < 1) {
                $(item).show();
            } else {
                $(item).hide();
            }
        });
    });
});