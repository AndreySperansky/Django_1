window.onload = function () {

    // добавляем ajax-обработчик для обновления количества товара
    $('.basket_list').on('click', 'input[type="number"]', function (event) {
        var target_href = event.target;
        
        if (target_href) {
            $.ajax({
                url: "/basket/edit/" + target_href.name + "/" + target_href.value + "/",
                
                success: function (data) {
                    $('.basket_list').html(data.result);
                    console.log('ajax done');
                },
            });

        }
        event.preventDefault();
    });

     $('.basket_list').on('click', 'button[type="button"]', function (event) {

        var target_href = event.target;
        // alert(target_href.name);

        if (target_href) {
            $.ajax({
                url: "/basket/delete_ajax/" + target_href.name + "/",

                success: function (data) {
                    $('.basket_list').html(data.result);
                    console.log('ajax done');
                },
            });

        }
        event.preventDefault();
    });
    
}