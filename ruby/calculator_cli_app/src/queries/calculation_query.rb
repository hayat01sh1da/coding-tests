# frozen_string_literal: true
# rbs_inline: enabled

require 'net/http'
require 'json'

module Queries
  class CalculationQuery
    # @rbs seed: String
    # @rbs return: void
    def initialize(seed)
      @seed = seed
    end

    # @rbs num: Integer
    # @rbs return: Integer
    def f(num)
      if num.zero?
        1
      elsif num == 2
        2
      elsif num.even?
        f(num - 1) + f(num - 2) + f(num - 3) + f(num - 4)
      else
        ask_server(num)
      end
    end

    private

    attr_reader :seed

    # @rbs return: URI::Generic
    def uri
      @uri ||= URI.parse(ENV.fetch('CALCULATION_API'))
    end

    # @rbs num: Integer
    # @rbs return: Integer
    def ask_server(num)
      uri.query = URI.encode_www_form(seed:, n: num)
      req       = Net::HTTP::Get.new(uri)
      res       = Net::HTTP.start(uri.host.to_s, uri.port) { |http| http.request(req) }
      JSON.parse(res.body)['result']
    end
  end
end
