//     //application
$(function(){

    // $(document).pjax('a.pjax', '#listWrap', {
    //     timeout: 3000

    // });

    // $(document).on('pjax:send', function() {
    //     // $('#loadingWraper').show();
    //     console.log(1)
    //     return false;
    // })
    // $(document).on('pjax:complete', function() {
    //     $('#loadingWraper').hide()
    // })

    // $('body').bind('ajaxComplete', function(event, xhr) {
    //     if (xhr.getResponseHeader('x-pjax-title')) {
    //         $('title').text(xhr.getResponseHeader('x-pjax-title'));
    //     } else {
    //         $('title').text('sss');
    //     }
    // });



    $(".time").timeago();

    $('#listWrap li .title a').click(function(){
        var t = $(this),
            li = t.parents('li').eq(0),
            sub = li.find('.sub');
        li.toggleClass('opened');
    })

    
    var formOpen = false;
    $('.newJobBtn').click(function(){
        var t = $(this),
            i = t.find('i');

        if (formOpen == true){
            i.addClass('icon-plus').removeClass('icon-minus');
            formOpen = false;
        } else {
            i.addClass('icon-minus').removeClass('icon-plus');
            
            formOpen = true;
        }

        $('.publishBody').toggleClass('opened')
    })
})