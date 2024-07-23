from security_policy_checks import SecurityPolicyChecker
from net_share_checks import NetShareChecks

class PC_Check():
    # PC_01 최대암호사용기간 90일 이하
    def pc_01(self: str, file_path: str) -> int:
        checker = SecurityPolicyChecker(file_path)
        check_maximum_password_age = checker._check_policy('MaximumPasswordAge', 90, lambda value, policy_value: value <= policy_value)
        return check_maximum_password_age

    def pc_02(self: str, file_path: str) -> int:
        checker = SecurityPolicyChecker(file_path)
        check_minimum_password_length = checker._check_policy('MinimumPasswordLength', 8, lambda value, policy_value: value >= policy_value)
        check_password_complexity = checker._check_policy('PasswordComplexity', 1, lambda value, policy_value: value == policy_value)
        return check_password_complexity and check_minimum_password_length

    def pc_03(self, file_path: str) -> int:
        checker = NetShareChecks(file_path)
        checker_netshare = checker._get_netshare_value()
        return checker_netshare