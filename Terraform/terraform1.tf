resource "local_file" "things-to-do" {
  filename     = "/root/things-to-do.txt"
  content  = "Clean my room before Christmas\nComplete the CKA Certification!"
}