#!/usr/bin/env -S python3 -B -u

class PythonPackageManager(object):
    def run(self):
        print("")
        print("Usage: ppm <command>")
        #print("where <command> is one of:")
        #print("    access, adduser, audit, bin, bugs, c, cache, ci, cit,")
        #print("    clean-install, clean-install-test, completion, config,")
        #print("    create, ddp, dedupe, deprecate, dist-tag, docs, doctor,")
        #print("    edit, explore, fund, get, help, help-search, hook, i, init,")
        #print("    install, install-ci-test, install-test, it, link, list, ln,")
        #print("    login, logout, ls, org, outdated, owner, pack, ping, prefix,")
        #print("    profile, prune, publish, rb, rebuild, repo, restart, root,")
        #print("    run, run-script, s, se, search, set, shrinkwrap, star,")
        #print("    stars, start, stop, t, team, test, token, tst, un,")
        #print("    uninstall, unpublish, unstar, up, update, v, version, view,")
        #print("    whoami")
        #print("")
        #print("ppm <command> -h  quick help on <command>")
        #print("ppm -l            display full usage info")
        #print("ppm help <term>   search for help on <term>")
        #print("ppm help npm      involved overview")
        #print("")
        #print("Specify configs in the ini-formatted file:")
        #print("    ~/.ppmrc")
        #print("or on the command line via: ppm <command> --key value")
        #print("Config info can be viewed via: ppm help config")
        print("")
        print("ppm@{0} {1}".format("1.0.0", ""))


def main():
    ppm = PythonPackageManager()
    ppm.run()
    return 0

if __name__ == "__main__":
    exit(main())