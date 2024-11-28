$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    // console.log(id)
    var eml = this.parentNode.children[2]

    $.ajax({
        type: "GET",
        url: "/plus-cart",
        data: {
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById("total_amount").innerText = data.total_amount
            document.getElementById("shipping_charge").innerText = data.shipping_charge
            document.getElementById("grand_total_amount").innerText = data.grand_total_amount

        }
    },)
})

$('.minus-cart').click(function () {
    var id = $(this).attr("pid").toString();
    // console.log(id)
    var eml = this.parentNode.children[2]

    $.ajax({
        type: "GET",
        url: "/minus-cart",
        data: {
            prod_id: id
        },
        success: function (data) {
            eml.innerText = data.quantity
            document.getElementById("total_amount").innerText = data.total_amount
            document.getElementById("shipping_charge").innerText = data.shipping_charge
            document.getElementById("grand_total_amount").innerText = data.grand_total_amount

        }
    },)
})

$('.remove-from-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var eml = this
    // console.log(id)

    $.ajax({
        type: "GET",
        url: "/remove-from-cart",
        data: {
            prod_id: id
        },
        success: function (data) {
            document.getElementById("total_amount").innerText = data.total_amount
            document.getElementById("shipping_charge").innerText = data.shipping_charge
            document.getElementById("grand_total_amount").innerText = data.grand_total_amount
            eml.parentNode.parentNode.parentNode.parentNode.remove()

        }
    },)
})




