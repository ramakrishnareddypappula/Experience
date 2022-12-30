resource "local_file" "name" {
    filename =  var.filename[count.index]
    count = length(var.filename)
    sensitive_content = "password: S3cr3tP@ssw0rd"

}




variables.tf
variable "filename"{
    default = [
        "/root/user-data/a.txt",
        "/root/user-data/b.txt",
        "/root/user-data/c.txt"
    ]
}

# resource will be create as list as opposed to map.