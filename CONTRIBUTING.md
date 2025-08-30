# 🤝 Contributing to CloudSec

Thank you for considering contributing to **CloudSec**!  
We welcome contributions in the form of automation scripts, IaC modules, documentation, detection rules, and best practices.  

---

## 📌 How to Contribute

1. **Fork the repository**  
   - Create your own fork and clone it locally.

2. **Create a feature branch**  
   ```bash
   git checkout -b feature/my-feature
   ```

3. **Follow the repo structure**  
   - Place automation under `automation/` (e.g., `automation/aws/s3/`).  
   - Place Terraform modules under `terraform/`.  
   - Add documentation under `docs/`.  
   - Policies should go under `policies/`.  

4. **Write clean code**  
   - Follow security best practices (least privilege, no secrets in code).  
   - Add comments and logging where applicable.  
   - Use `.gitignore` to avoid committing sensitive files.  

5. **Test your contribution**  
   - Validate scripts and IaC modules.  
   - Ensure CI/CD pipelines pass.  

6. **Submit a Pull Request (PR)**  
   - Provide a clear description of your changes.  
   - Reference any related issues.  
   - Wait for review before merging.  

---

## ✅ Contribution Guidelines
- Follow the **principle of least privilege** for IAM roles and policies.  
- **Do not commit secrets** (use environment variables or secret managers).  
- All scripts must include a **README.md** explaining usage.  
- Use **Python 3** for automation scripts and **Terraform** for IaC modules.  
- Add tests or validation steps whenever possible.  

---

## 🛡️ Security Issues
If you discover a security issue, **do not open a public issue**.  
Instead, report it responsibly by contacting the maintainers.  

---

## 📜 License
By contributing, you agree that your contributions will be licensed under the same [MIT License](./LICENSE) as the project.
