variable "allowed_ip_cidr" {
  description = "Public IPv4 address permitted to test the API, in /32 CIDR format"
  type        = string
  default     = null

  validation {
    condition = (
      var.allowed_ip_cidr == null ||
      can(cidrnetmask(var.allowed_ip_cidr))
    )
    error_message = "Enter a valid IPv4 CIDR such as 198.51.100.10/32."
  }
}

resource "aws_vpc_security_group_ingress_rule" "api_test" {
  count = var.allowed_ip_cidr == null ? 0 : 1

  security_group_id = aws_security_group.api.id
  description       = "Temporary restricted API testing access"
  cidr_ipv4         = var.allowed_ip_cidr
  from_port         = 8000
  to_port           = 8000
  ip_protocol       = "tcp"
}
