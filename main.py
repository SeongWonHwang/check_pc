from output_exportpolicy import export_securitypolicy
from output_exportpolicy import export_netshare
from result_write import write_result
from check_pc import PC_Check


def main():
    security_config_file_path = 'C:\\securitypolicy_export.inf'
    netshare_file_path = 'C:\\netshare_export.inf'
    result_file_path = 'C:\\result.txt'

    # 정책 체크결과를 만족, 불만족으로 변환
    def _check_policy_result(check_result: int) -> str:
        return "만족" if check_result else "불만족"

    try:
        # 정책 내보내기
        export_securitypolicy()
        export_netshare()

        pc_check = PC_Check()

        # 각 정책 체크
        results = [
            f"PC-01 패스워드의 주기적 변경: {_check_policy_result(pc_check.pc_01(security_config_file_path))}",
            f"PC-02 패스워드 정책이 해당 기관의 보안 정책에 적합하게 설정: {_check_policy_result(pc_check.pc_02(security_config_file_path))}",
            f"PC-03 공유폴더 제거: {_check_policy_result(pc_check.pc_03(netshare_file_path))}"
        ]
        # 결과를 result.txt 파일에 기록
        write_result(result_file_path, results)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
