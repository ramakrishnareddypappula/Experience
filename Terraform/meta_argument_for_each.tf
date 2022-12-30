resource "local_file" "pet" {
  filename = each.value
  for_each = var.filename
}

variable "filename" {
  type = set(string)
  default = [
    "/root/dog.txt",
    "/root/cat.txt"

  ]
}