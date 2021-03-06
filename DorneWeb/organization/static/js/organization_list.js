$(function () {
    $('#organization_list_table tbody').on('click', '.delete_org', function () {
        let organization_id = $(this).data('org_id');
        let url = '/organization/ajax/organization/' + organization_id + '/delete/';
        Swal({
            title: "确定删除",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "确定",
            cancelButtonText: "取消",
        }).then(function (result) {
            if (result.value) {
                $.post(url, {}, function (data) {
                    if (data.status) {
                        //Swal('成功', '删除组织成功', 'success').then(function () {
                           //window.location.reload();
                        //});
                        toastr.success('删除组织成功');
                        refresh(500);
                    } else {
                        //Swal('出错', data.errmsg, 'error').then(function () {
                            //window.location.reload();
                        //});
                        toastr.error('删除组织出错:' + data.errmsg);
                    }
                })
            } else if (result.dismiss === Swal.DismissReason.cancel) {

            }
        });
    })
});