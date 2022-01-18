
/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    EDIT ITEM FUCNTION
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<*/
function editItem(item) {

}




/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    DELETE ITEM FUCNTION
    - function fires a sweet alert
    - dialogue box that on confirm
    - sends a resful get request
    - to crud to delete the passed item id
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<*/
function deleteItem( item_id)  {
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            $.get("/restful_api/delete_item/", { item_id: item_id }, function(data) {
                // if data has item => successfull ? else error
                if (data.item) {
                    // remove row from table
                    $(`#row${item_id}`).remove();
                    Swal.fire(
                        'Deleted!',
                        `${data.item} has been deleted.`,
                        'success'
                    )
                } else{
                    Swal.fire(
                        'Something Went Wrong!',
                        `${data.error}`,
                        'error'
                    )
                }
            })
            .fail(function(data){
                Swal.fire(
                    'Something Went Wrong!',
                    `${data.error}`,
                    'error'
                )
            });
        }
    })
}



/*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    LOGOUT MODAL | SWEET ALERT

    -function fires confirmation alert
    with a link to logout url on confirm
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<*/
$( "#logout" ).click(function() {
     Swal.fire({
        icon: 'question',
        title: 'Logout...',
        text: 'Are You Sure You Want to Logout.',
        showCloseButton: true,
        showCancelButton: true,
        focusConfirm: true,
        confirmButtonColor: 'aqua',
        cancelButtonColor: '#d33',
        confirmButtonText:
            `<a href="/accounts/logout/"><i class="fa fa-power-off"></i> Logout</a>`,
        footer: `<a href="{% url 'lock' %}">Go to Lockscreen instead</a>`
    })

})



/*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    INITIATING DATA TABLE
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<*/
$(function () {
        $("#example1").DataTable({
            "responsive": true, "lengthChange": true, "autoWidth": false,
            "autoWidth": true, "info": true,
            "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
        }).buttons().container().appendTo('#example1_wrapper .col-md-6:eq(0)');
        $('#example2').DataTable({
            "paging": true,
            "lengthChange": true,
            "searching": true,
            "ordering": true,
            "info": true,
            "autoWidth": true,
            "responsive": true,
        });
});



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    PAGE REFRESH SCRIPT

    - any button in the app with an id of refresh
    - calls this function.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<*/
var refresh_button = document.getElementById("refresh");

refresh_button.addEventListener('click', function () {
    document.location.reload(force=true)
})



/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    APPEND VEW ITEM TO TABLE
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<*/
function appendToItemTable(item) {
    $('#example1 > tbody:last-child').append(`
                    <tr>
                        <td>${item.id}</td>
                        <td><a href="#!">${item.item_name}</a></td>
                        <td>${item.description}</td>
                        <td>${item.quantity}</td>
                        <td>${item.unit_price}</td>
                        <td>${item.value}</td>
                        <td><button class="btn btn-info">Avilable</button></td>
                        <td>${item.category}</td>
                        <td class="row">
                            <button class="btn btn-outline-secondary" data-toggle="modal" data-target="#editItemModal${item.id}"><i class="fa fa-edit text-green"></i></button>
                            <button onclick="deleteItem(${item.id});" class="btn btn-outline-secondary" style="margin: 2px"><i class="fa fa-trash text-red"></i></button>
                        </td>
                    </tr>
`);
}


/* >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    ADD ITEM CLEAR FORM FUNCTION
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<*/
function resetForm(form_id) {
    var form = document.getElementById(form_id);
    form.reset()

}
