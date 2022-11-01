window.addEventListener("load", function () {
amenities = document.querySelector(".amenities");

states = document.querySelector(".locations");
popover1 = document.getElementsByClassName("popover")[0];
popover2 = document.getElementsByClassName("popover")[1];
dropList = this.document.getElementsByClassName("droplist")[0];

states.addEventListener("mouseover", (event) => {
dropList.classList.add("show");
});

states.addEventListener("mouseout", (event) => {
dropList.classList.remove("show");
});

amenities.addEventListener("mouseover", (event) => {
dropList.classList.add("show");
});

amenities.addEventListener("mouseout", (event) => {
dropList.classList.remove("show");
});
});
